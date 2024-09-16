#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/otgw/otgw.h"

namespace esphome {
namespace otgw {

class OpenThermGatewaySensor : public sensor::Sensor, public Component {
    public:
        void setup() override;
        void dump_config() override;
        void set_parent(OpenThermGateway *parent) { this->parent_ = parent; }
        void set_data_id(uint8_t data_id) { this->data_id_ = data_id; };
        void set_data_type(OpenThermDataType data_type) { this->data_type_ = data_type; }
        void set_clear_on_timeout(bool clear_on_timeout) { this->clear_on_timeout_ = clear_on_timeout; }
    protected:
        OpenThermGateway *parent_;
        uint8_t data_id_;
        OpenThermDataType data_type_;
        bool clear_on_timeout_;

        void on_otmessage(const OpenThermMessage &message);
        void on_timeout();
};

} // namespace otgw
} // namespace esphome
