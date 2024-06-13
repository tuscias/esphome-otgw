import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import (
    CONF_ID,
    DEVICE_CLASS_COLD,
    DEVICE_CLASS_HEAT,
    DEVICE_CLASS_PROBLEM,
    ENTITY_CATEGORY_DIAGNOSTIC,
)
from .. import otgw_ns, CONF_OTGW_ID, OpenThermGateway
from dataclasses import dataclass

DEPENDENCIES = ["otgw"]
CODEOWNERS = ["@mvdnes"]

OpenThermGatewayBinarySensor = otgw_ns.class_("OpenThermGatewayBinarySensor", binary_sensor.BinarySensor, cg.Component)

SENSOR_FAULT_INDICATION = "fault_indication"
SENSOR_CH_ACTIVE = "ch_active"
SENSOR_DHW_ACTIVE = "dhw_active"
SENSOR_FLAME_STATUS = "flame_status"
SENSOR_COOLING_STATUS = "cooling_status"
SENSOR_CH2_ACTIVE = "ch2_active"
SENSOR_DIAGNOSTIC_INDICATION = "diagnostic_indication"


@dataclass
class OpenThermGatewayBinarySensorConfig:
    data_id: int
    flag_bit: int
    clear_on_timeout: bool = True


SENSOR_CONFIG = {
    SENSOR_FAULT_INDICATION: OpenThermGatewayBinarySensorConfig(0, 0, clear_on_timeout=False),
    SENSOR_CH_ACTIVE: OpenThermGatewayBinarySensorConfig(0, 1),
    SENSOR_DHW_ACTIVE: OpenThermGatewayBinarySensorConfig(0, 2),
    SENSOR_FLAME_STATUS: OpenThermGatewayBinarySensorConfig(0, 3),
    SENSOR_COOLING_STATUS: OpenThermGatewayBinarySensorConfig(0, 4),
    SENSOR_CH2_ACTIVE: OpenThermGatewayBinarySensorConfig(0, 5),
    SENSOR_DIAGNOSTIC_INDICATION: OpenThermGatewayBinarySensorConfig(0, 6, clear_on_timeout=False),
}


CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(CONF_OTGW_ID): cv.use_id(OpenThermGateway),

    cv.Optional(SENSOR_FAULT_INDICATION): binary_sensor.binary_sensor_schema(
        OpenThermGatewayBinarySensor,
        device_class=DEVICE_CLASS_PROBLEM,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
    ),
    cv.Optional(SENSOR_CH_ACTIVE): binary_sensor.binary_sensor_schema(
        OpenThermGatewayBinarySensor,
        device_class=DEVICE_CLASS_HEAT,
    ),
    cv.Optional(SENSOR_DHW_ACTIVE): binary_sensor.binary_sensor_schema(
        OpenThermGatewayBinarySensor,
        device_class=DEVICE_CLASS_HEAT,
    ),
    cv.Optional(SENSOR_FLAME_STATUS): binary_sensor.binary_sensor_schema(
        OpenThermGatewayBinarySensor,
        device_class=DEVICE_CLASS_HEAT,
    ),
    cv.Optional(SENSOR_COOLING_STATUS): binary_sensor.binary_sensor_schema(
        OpenThermGatewayBinarySensor,
        device_class=DEVICE_CLASS_COLD,
    ),
    cv.Optional(SENSOR_CH2_ACTIVE): binary_sensor.binary_sensor_schema(
        OpenThermGatewayBinarySensor,
        device_class=DEVICE_CLASS_HEAT,
    ),
    cv.Optional(SENSOR_DIAGNOSTIC_INDICATION): binary_sensor.binary_sensor_schema(
        OpenThermGatewayBinarySensor,
        device_class=DEVICE_CLASS_PROBLEM,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
    ),
})

async def to_code(config):
    parent = await cg.get_variable(config[CONF_OTGW_ID])

    for key, conf in config.items():
        if not isinstance(conf, dict):
            continue
        id = conf[CONF_ID]
        if id and id.type == binary_sensor.BinarySensor:
            sens = await binary_sensor.new_binary_sensor(conf)
            await cg.register_component(sens, conf)
            sensorconfig = SENSOR_CONFIG[key]
            cg.add(sens.set_parent(parent))
            cg.add(sens.set_data_id(sensorconfig.data_id))
            cg.add(sens.set_flag_bit(sensorconfig.flag_bit))
            cg.add(sens.set_clear_on_timeout(sensorconfig.clear_on_timeout))
