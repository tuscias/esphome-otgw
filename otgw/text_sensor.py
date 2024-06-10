import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import text_sensor
from esphome.const import (
    CONF_ID,
    ENTITY_CATEGORY_DIAGNOSTIC,
)
from . import OpenThermGateway

AUTO_LOAD = ["otgw"]

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.use_id(OpenThermGateway),

    cv.Optional("version"): text_sensor.text_sensor_schema(
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
    ),
})

async def to_code(config):
    var = await cg.get_variable(config[CONF_ID])

    text_sensors = []
    for key, conf in config.items():
        if not isinstance(conf, dict):
            continue
        id = conf[CONF_ID]
        if id and id.type == text_sensor.TextSensor:
            sens = await text_sensor.new_text_sensor(conf)
            cg.add(getattr(var, f"set_{key}_sensor")(sens))
