#include "binary_sensor.h"

namespace esphome {
namespace otgw {

static const char *const TAG = "otgw_binary_sensor";


void OpenThermGatewayBinarySensor::setup() {
    this->parent_->register_listener(
        this->data_id_,
        [this](const OpenThermMessage &message) { this->on_otmessage(message); }
    );

    if (this->clear_on_timeout_) {
        this->parent_->register_timeout_listener([this]() { this->on_timeout(); });
    }
}

void OpenThermGatewayBinarySensor::on_otmessage(const OpenThermMessage &message) {
    bool value = (message.value_u16 >> this->flag_bit_) & 1;
    this->publish_state(value);
}

void OpenThermGatewayBinarySensor::on_timeout() {
    this->publish_state(false);
}

} // namespace otgw
} // namespace esphome
