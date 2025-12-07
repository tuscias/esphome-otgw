#pragma once

#include "esphome/core/component.h"
#include "esphome/core/automation.h"
#include "otgw.h"

namespace esphome {
namespace otgw {

template<typename... Ts> class OpenThermGatewaySendCommandAction : public Action<Ts...> {
 public:
  explicit OpenThermGatewaySendCommandAction(OpenThermGateway *otgw) :otgw_(otgw) {}
  TEMPLATABLE_VALUE(std::string, command)
  TEMPLATABLE_VALUE(std::string, data)

  void play(const Ts &...x) override {
    auto command = this->command_.value(x...);
    auto data = this->data_.value(x...);
    this->otgw_->send_command(command, data);
  }

 protected:
  OpenThermGateway *otgw_;
};

}  // namespace empty_automation
}  // namespace esphome
