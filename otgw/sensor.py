import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_ID,
    DEVICE_CLASS_DURATION,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_PRESSURE,
    ENTITY_CATEGORY_DIAGNOSTIC,
    UNIT_HOUR,
    UNIT_CELSIUS,
    STATE_CLASS_TOTAL_INCREASING,
    STATE_CLASS_MEASUREMENT,
)
from . import OpenThermGateway

AUTO_LOAD = ["otgw"]

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.use_id(OpenThermGateway),

    cv.Optional("room_temperature"): sensor.sensor_schema(
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=2,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional("central_heating_water_pressure"): sensor.sensor_schema(
        unit_of_measurement='bar',
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_PRESSURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional("burner_operation_hours"): sensor.sensor_schema(
        unit_of_measurement=UNIT_HOUR,
        accuracy_decimals=0,
        device_class=DEVICE_CLASS_DURATION,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional("boiler_water_temperature"): sensor.sensor_schema(
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=0,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
})

async def to_code(config):
    var = await cg.get_variable(config[CONF_ID])

    text_sensors = []
    for key, conf in config.items():
        if not isinstance(conf, dict):
            continue
        id = conf[CONF_ID]
        if id and id.type == sensor.Sensor:
            sens = await sensor.new_sensor(conf)
            cg.add(getattr(var, f"set_sensor_{key}")(sens))
