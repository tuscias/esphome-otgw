#pragma once

#include "esphome/core/component.h"
#include "esphome/components/binary_sensor/binary_sensor.h"
#include "esphome/components/otgw/otgw.h"

namespace esphome {
namespace otgw {

class OpenThermGatewayBinarySensor : public binary_sensor::BinarySensor, public Component {
    public:
        void setup() override;
        void dump_config() override;
        void set_parent(OpenThermGateway *parent) { this->parent_ = parent; }
        void set_data_id(uint8_t data_id) { this->data_id_ = data_id; }
        void set_flag_bit(uint8_t flag_bit) { this->flag_bit_ = flag_bit; }
        void set_clear_on_timeout(bool clear_on_timeout) { this->clear_on_timeout_ = clear_on_timeout; }
    protected:
        OpenThermGateway *parent_;
        uint8_t data_id_;
        uint8_t flag_bit_;
        bool clear_on_timeout_;

        void on_otmessage(const OpenThermMessage &message);
        void on_timeout();
};

} // namespace otgw
} // namespace esphome
