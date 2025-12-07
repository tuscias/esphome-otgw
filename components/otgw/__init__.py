import esphome.config_validation as cv
import esphome.codegen as cg

from esphome.components import uart, sensor

from esphome.const import CONF_COMMAND, CONF_DATA, CONF_ID

from esphome import automation

CODEOWNERS = ["@mvdnes"]
DEPENDENCIES = ["uart"]
AUTO_LOAD = ["sensor", "text_sensor"]

otgw_ns = cg.esphome_ns.namespace("otgw")
OpenThermGateway = otgw_ns.class_("OpenThermGateway", uart.UARTDevice, cg.Component)
OpenThermGatewaySendCommandAction = otgw_ns.class_(
        "OpenThermGatewaySendCommandAction", automation.Action
)

CONF_OTGW_ID = "otgw_id"

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(OpenThermGateway),
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
    .extend(uart.UART_DEVICE_SCHEMA)
)

OPENTHERMGATEWAY_ACTION_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.use_id(OpenThermGateway),
            cv.Required(CONF_COMMAND): cv.templatable(cv.string),
            cv.Required(CONF_DATA): cv.templatable(cv.string),
        }
    )
)

@automation.register_action(
    "otgw.send_command",
    OpenThermGatewaySendCommandAction,
    OPENTHERMGATEWAY_ACTION_SCHEMA,
)
async def openthermgateway_send_command_action_to_code(config, action_id, template_arg, args):
    paren = await cg.get_variable(config[CONF_ID])
    var = cg.new_Pvariable(action_id, template_arg, paren)

    template_command = await cg.templatable(config[CONF_COMMAND], args, cg.std_string)
    cg.add(var.set_command(template_command))

    template_data = await cg.templatable(config[CONF_DATA], args, cg.std_string)
    cg.add(var.set_data(template_data))

    return var


FINAL_VALIDATE_SCHEMA = uart.final_validate_device_schema(
    "otgw",
    baud_rate=9600,
    data_bits=8,
    parity="NONE",
    stop_bits=1,
    require_rx=True,
    require_tx=True,
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])

    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)
