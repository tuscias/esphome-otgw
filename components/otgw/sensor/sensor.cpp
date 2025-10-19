#include "sensor.h"

namespace esphome {
namespace otgw {

static const char *const TAG = "otgw.sensor";

static const float NaN = std::numeric_limits<float>::quiet_NaN();

void OpenThermGatewaySensor::setup() {
    this->parent_->register_listener(
        this->data_id_,
        [this](const OpenThermMessage &message) { this->on_otmessage(message); }
    );

    if (this->clear_on_timeout_) {
        this->parent_->register_timeout_listener([this]() { this->on_timeout(); });
    }
}

void OpenThermGatewaySensor::dump_config() {
    LOG_SENSOR("", "OpenThermGatewaySensor", this);
}

void OpenThermGatewaySensor::on_otmessage(const OpenThermMessage &message) {
    float value = NaN;
    switch (this->data_type_) {
        case OpenThermDataType::U16:
            value = message.value_u16;
            break;
        case OpenThermDataType::F88:
            value = message.value_f88;
            break;
        case OpenThermDataType::S16:
            value = static_cast<int16_t>(message.value_u16);
            break;
    }
    this->publish_state(value);
}

void OpenThermGatewaySensor::on_timeout() {
    this->publish_state(NaN);
}

} // namespace otgw
} // namespace esphome
