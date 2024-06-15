#pragma once

#include <vector>

#include "esphome/components/uart/uart.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/text_sensor/text_sensor.h"

namespace esphome {
namespace otgw {

const int OTGW_BUFFER_SIZE = 128;
const int OTGW_BUFFER_INVALID = -1;
const int OTGW_MAX_LINE_DURATION_MS = 150;
const int OTGW_COMMAND_RESPONSE_MAX_DURATION_MS = 5000;
const int OTGW_OTMESSAGE_TIMEOUT_MS = 10000; // spec: 1s +/- 15%, we wait 10s
const int OTGW_TARGET_TEMPERATURE_MAX_TRIES = 5;

enum class OpenThermDataType {
    U16,
    F88,
};

struct OpenThermMessage {
    uint8_t msg_type;
    uint8_t data_id;

    uint16_t value_u16;
    uint8_t value_lb;
    uint8_t value_hb;
    float value_f88;

    OpenThermMessage(uint32_t frame) {
        this->msg_type = (frame >> 28) & 0x7;
        this->data_id = (frame >> 16) & 0xFF;
        this->value_u16 = frame & 0xFFFF;
        this->value_hb = (this->value_u16 >> 8) & 0xFF;
        this->value_lb = this->value_u16 & 0xFF;
        this->value_f88 = (int8_t)this->value_hb + (float)this->value_lb / 256.0;
    }
};

struct OpenThermMessageListener {
    uint8_t data_id;
    std::function<void(const OpenThermMessage&)> on_otmessage;
};

struct TimeoutListener {
    std::function<void(void)> on_timeout;
};

class OpenThermGateway : public Component, public uart::UARTDevice {
public:
    OpenThermGateway() {
        this->buffer_pos = 0;
        this->state = 0;
    }
    void setup() override;
    void loop() override;
    float get_setup_priority() const override { return setup_priority::DATA; }
    // TODO: void dump_config() override;

    void register_listener(
            uint8_t data_id,
            const std::function<void(OpenThermMessage)> &on_otmessage) {
        OpenThermMessageListener listener;
        listener.data_id = data_id;
        listener.on_otmessage = on_otmessage;
        this->listeners_.push_back(listener);
    }

    void register_timeout_listener(const std::function<void()> &on_timeout) {
        TimeoutListener timeout_listener;
        timeout_listener.on_timeout = on_timeout;
        this->on_timeout_listeners_.push_back(timeout_listener);
    }

    void set_sensor_version(text_sensor::TextSensor *sensor) { this->sensor_version_ = sensor; }

    void set_room_temperature(float temperature, bool constant);
protected:
    int buffer_pos;
    char buffer[OTGW_BUFFER_SIZE];
    uint32_t buffer_start_time;

    int state;
    const uint8_t* last_command_sent{nullptr};
    uint32_t command_request_start_time;

    uint32_t last_valid_otmessage;

    float target_temperature_;
    int target_temperature_tries_;

    text_sensor::TextSensor *sensor_version_{nullptr};
    std::vector<OpenThermMessageListener> listeners_;
    std::vector<TimeoutListener> on_timeout_listeners_;

    void read_incoming_data();
    void parse_buffer();
    bool parse_command_response();
    void parse_otmessage();
    void send_command(const uint8_t* command, const uint8_t* data, size_t datalen);
    bool should_send_command();
    bool response_is_from_last_command();
    void request_version();
    void set_printsummary();
    void send_request_target_temperature(bool constant);
    bool command_response_startswith(const char* startstring, int startstringlen);
    bool command_response_equals(const char* contents, int contentslen);
    void go_idle();
    void check_otmessage_timeout();
};

}
}
