#pragma once

#include "esphome/core/component.h"
#include "esphome/components/climate/climate.h"
#include "esphome/components/otgw/otgw.h"

namespace esphome {
namespace otgw {

class OpenThermGatewayClimateThermostat : public climate::Climate, public Component {
    public:
        void setup() override;
        // TODO: void dump_config() override;
        climate::ClimateTraits traits() override;
        void control(const climate::ClimateCall& call) override;

        void set_parent(OpenThermGateway *parent) { this->parent_ = parent; }
        void set_target_temperature_constant(bool constant) { this->target_temperature_constant_ = constant; }
    protected:
        OpenThermGateway *parent_;
        bool target_temperature_constant_;

        void on_otmessage(const OpenThermMessage &message);
        void on_timeout();
};

} // namespace otgw
} // namespace esphome
