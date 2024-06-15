#include "otgw.h"

#include <sstream>
#include <iomanip>

namespace esphome {
namespace otgw {

static const char *const TAG = "otgw";

static const size_t OTGW_COMMAND_SIZE = 2;
static const uint8_t OTGW_COMMAND_PRINT_REPORT[] = "PR";
static const uint8_t OTGW_COMMAND_PRINT_SUMMARY[] = "PS";
static const uint8_t OTGW_COMMAND_TARGET_TEMPERATURE_TEMPORARY[] = "TT";
static const uint8_t OTGW_COMMAND_TARGET_TEMPERATURE_CONSTANT[] = "TC";

static const uint8_t OTGW_REPORT_KIND_ABOUT = 'A';

static const int STATE_INITIAL = 0;
static const int STATE_IDLE = 1;
static const int STATE_REQUEST_VERSION = 10;
static const int STATE_REQUEST_PRINT_SUMMARY = 20;
static const int STATE_REQUEST_TARGET_TEMPERATURE_TEMPORARY = 30;
static const int STATE_REQUEST_TARGET_TEMPERATURE_CONSTANT = 31;

void OpenThermGateway::setup() {
    // Ensure any garbage is cleared by sending a newline
    this->write_byte('\r');
}

void OpenThermGateway::loop() {
    this->read_incoming_data();

    switch (this->state) {
        case STATE_IDLE:
            this->check_otmessage_timeout();
            break;
        case STATE_INITIAL:
            this->state = STATE_REQUEST_VERSION;
            // fallthrough
        case STATE_REQUEST_VERSION:
            this->request_version();
            break;
        case STATE_REQUEST_PRINT_SUMMARY:
            this->set_printsummary();
            break;
        case STATE_REQUEST_TARGET_TEMPERATURE_TEMPORARY:
            this->send_request_target_temperature(false);
            break;
        case STATE_REQUEST_TARGET_TEMPERATURE_CONSTANT:
            this->send_request_target_temperature(true);
            break;
        default:
            ESP_LOGE(TAG, "State machine was in illegal state %d! Resetting to initial state.", this->state);
            this->state = STATE_INITIAL;
    }
}

void OpenThermGateway::read_incoming_data() {
    while (this->available() > 0) {
        char c = this->read();

        if (this->buffer_pos == OTGW_BUFFER_INVALID) {
            // if the current line is invalid, ignore everything until a new line starts
            if (c == '\r') {
                this->buffer_pos = 0;
            }
        }
        else {
            if (c == '\r') {
                // carriage-return marks end of line
                ESP_LOGD(TAG, "Read line: '%.*s'", this->buffer_pos, this->buffer);
                this->parse_buffer();
                this->buffer_pos = 0;
            }
            else if (c == '\n' && this->buffer_pos == 0) {
                // ignore the \n of \r\n
            }
            else if (this->buffer_pos < OTGW_BUFFER_SIZE && (c & 0x80) == 0) {
                this->buffer[this->buffer_pos] = c;
                this->buffer_pos += 1;

                if (this->buffer_pos == 1) {
                    this->buffer_start_time = millis();
                }
                else if (millis() - this->buffer_start_time > OTGW_MAX_LINE_DURATION_MS) {
                    this->buffer_pos = OTGW_BUFFER_INVALID;
                    ESP_LOGW(TAG, "Current line took too long.");
                }
            }
            else {
                // line was too long or contained invalid characters. Ignore until next '\r'
                this->buffer_pos = OTGW_BUFFER_INVALID;
            }
        }
    }
}

void OpenThermGateway::parse_buffer() {
    if (this->buffer_pos == OTGW_BUFFER_INVALID || this->buffer_pos > OTGW_BUFFER_SIZE) {
        // buffer was invalid, ignore
        return;
    }

    if (this->parse_command_response()) {
        // Parsed the message succesfully
        return;
    }

    this->parse_otmessage();
}

bool OpenThermGateway::parse_command_response() {
    // Check for a command response. It should be at least four bytes long and start with 'XY: '
    if (this->buffer_pos < 4 || this->buffer[2] != ':' || this->buffer[3] != ' ') {
        return false;
    }

    if (!this->response_is_from_last_command()) {
        ESP_LOGW(TAG, "Response to command '%.2s' was unexpected", this->buffer);
        return true;
    }

    switch (this->state) {
        case STATE_REQUEST_VERSION:
            if (this->command_response_startswith("A=", 2)) {
                const char* versionstart = &this->buffer[4 + 2];
                int versionlen = this->buffer_pos - 4 - 2;
                std::string version_str(versionstart, versionlen);
                ESP_LOGI(TAG, "Got version: '%s'", version_str.c_str());
                if (version_str.size() > 0 && this->sensor_version_ != nullptr) {
                    this->sensor_version_->publish_state(version_str);
                }
                this->last_command_sent = nullptr;
                this->state = STATE_REQUEST_PRINT_SUMMARY;
            }
            break;
        case STATE_REQUEST_PRINT_SUMMARY:
            if (this->command_response_equals("0", 1)) {
                ESP_LOGI(TAG, "PrintSummary succesfully set");
                this->last_command_sent = nullptr;
                this->go_idle();
            }
            break;
        case STATE_REQUEST_TARGET_TEMPERATURE_CONSTANT:
        case STATE_REQUEST_TARGET_TEMPERATURE_TEMPORARY:
            ESP_LOGI(TAG, "Temperature set");
            this->last_command_sent = nullptr;
            this->go_idle();
            break;
        default:
            break;
    }

    return true;
}

void OpenThermGateway::parse_otmessage() {
    // Message structure is X01234567 where X is the type and
    //  01234567 is a 32-bit payload encoded in uppercase hexadecimal
    if (this->buffer_pos != 9) {
        return;
    }

    char otgw_message_type = this->buffer[0];

    // Possible otgw_message_type:
    // T  Thermostat request
    // B  Boiler answer
    // R  Request inserted by OTGW to boiler
    // A  Answer inserted by OTGW to thermostat
    // E  Errornous message

    // Continue only for T and B messages, as the other ones are faked or errorneous
    if (otgw_message_type != 'T' && otgw_message_type != 'B') {
        return;
    }

    // Check and convert 8 hexadecimal characters
    uint32_t frame = 0;
    for (int i = 1; i < 9; ++i) {
        char cur = this->buffer[i];
        uint32_t hex_value = 0;
        if (cur >= '0' && cur <= '9') {
            hex_value = cur - '0';
        }
        else if (cur >= 'A' && cur <= 'F') {
            hex_value = cur - 'A' + 10;
        }
        else {
            return;
        }
        frame = frame * 16 + hex_value;
    }

    if (otgw_message_type == 'T') {
        this->last_valid_otmessage = millis();
    }

    OpenThermMessage otmessage(frame);

    if (otmessage.msg_type != 1 && otmessage.msg_type != 4) { // write-data or read-ack
        return;
    }

    for (auto &listener : this->listeners_) {
        if (listener.data_id == otmessage.data_id) {
            listener.on_otmessage(otmessage);
        }
    }
}

void OpenThermGateway::send_command(const uint8_t* command, const uint8_t* data, size_t datalen) {
    // Send the command over serial
    this->write_array(command, OTGW_COMMAND_SIZE);
    this->write_byte('=');
    this->write_array(data, datalen);
    this->write_byte('\r');
    ESP_LOGD(TAG, "Sent command %.2s=%.*s", command, datalen, data);

    // Setup the command parser
    this->last_command_sent = command;
    this->command_request_start_time = millis();
}

bool OpenThermGateway::should_send_command() {
    // Send a command if:
    //   - It has never been sent, indicated by last_command_sent == nullptr
    //   - The command has timed out
    if (this->last_command_sent == nullptr) {
        return true;
    }
    else if (millis() - this->command_request_start_time > OTGW_COMMAND_RESPONSE_MAX_DURATION_MS) {
        ESP_LOGW(TAG, "Timeout waiting for command response to %.2s", this->last_command_sent);
        return true;
    }
    return false;
}

bool OpenThermGateway::response_is_from_last_command() {
    if (this->last_command_sent == nullptr) return false;
    return this->buffer[0] == this->last_command_sent[0] && this->buffer[1] == this->last_command_sent[1];
}

void OpenThermGateway::request_version() {
    if (this->should_send_command()) {
        this->send_command(OTGW_COMMAND_PRINT_REPORT, &OTGW_REPORT_KIND_ABOUT, 1);
    }
}

void OpenThermGateway::set_printsummary() {
    if (this->should_send_command()) {
        this->send_command(OTGW_COMMAND_PRINT_SUMMARY, (const uint8_t*)"0", 1);
    }
}

void OpenThermGateway::send_request_target_temperature(bool constant) {
    if (this->should_send_command()) {
        if (this->target_temperature_tries_ == OTGW_TARGET_TEMPERATURE_MAX_TRIES) {
            ESP_LOGW(TAG, "Maximum number of tries exceeded for setting target temperature. Aborting.");
            this->last_command_sent = nullptr;
            this->go_idle();
        }
        else {
            this->target_temperature_tries_ += 1;
            const uint8_t* command;
            if (!constant) {
                command = OTGW_COMMAND_TARGET_TEMPERATURE_TEMPORARY;
            }
            else {
                command = OTGW_COMMAND_TARGET_TEMPERATURE_CONSTANT;
            }
            std::stringstream ss;
            ss << std::fixed << std::setprecision(2) << this->target_temperature_;
            std::string mystring = ss.str();
            this->send_command(command, (uint8_t*)mystring.c_str(), mystring.size());
        }
    }
}

bool OpenThermGateway::command_response_startswith(const char* startstring, int startstringlen) {
    if (this->buffer_pos < startstringlen + 4) {
        return false;
    }
    for (int i = 0; i < startstringlen; ++i) {
        if (this->buffer[i + 4] != startstring[i]) {
            return false;
        }
    }
    return true;
}

bool OpenThermGateway::command_response_equals(const char* contents, int contentslen) {
    if (this->buffer_pos != contentslen + 4) {
        return false;
    }
    return this->command_response_startswith(contents, contentslen);
}

void OpenThermGateway::go_idle() {
    this->state = STATE_IDLE;
    this->last_valid_otmessage = millis();
}

void OpenThermGateway::check_otmessage_timeout() {
    if (millis() - this->last_valid_otmessage > OTGW_OTMESSAGE_TIMEOUT_MS) {
        ESP_LOGW(TAG, "Timeout waiting for valid otmessage from master, resetting state.");
        this->state = STATE_INITIAL;
        for (auto &listener: this->on_timeout_listeners_) {
            listener.on_timeout();
        }
    }
}

void OpenThermGateway::set_room_temperature(float temperature, bool constant) {
    if (this->state != STATE_IDLE) {
        return;
    }

    if (constant) {
        this->state = STATE_REQUEST_TARGET_TEMPERATURE_CONSTANT;
    }
    else {
        this->state = STATE_REQUEST_TARGET_TEMPERATURE_TEMPORARY;
    }

    this->target_temperature_tries_ = 0;
    this->target_temperature_ = temperature;
}

}  // namespace esphome
}  // namespace otgw
