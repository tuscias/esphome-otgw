import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_ID,
    DEVICE_CLASS_DURATION,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_PRESSURE,
    ENTITY_CATEGORY_DIAGNOSTIC,
    UNIT_CELSIUS,
    UNIT_EMPTY,
    UNIT_HOUR,
    UNIT_PERCENT,
    STATE_CLASS_TOTAL_INCREASING,
    STATE_CLASS_MEASUREMENT,
)
from .. import otgw_ns, CONF_OTGW_ID, OpenThermGateway
from dataclasses import dataclass

DEPENDENCIES = ["otgw"]
CODEOWNERS = ["@mvdnes"]

OpenThermGatewaySensor = otgw_ns.class_("OpenThermGatewaySensor", sensor.Sensor, cg.Component)


SENSOR_CONTROL_SETPOINT = "control_setpoint"
SENSOR_ROOM_SETPOINT = "room_setpoint"
SENSOR_CENTRAL_HEATING_WATER_PRESSURE = "central_heating_water_pressure"
SENSOR_ROOM_TEMPERATURE = "room_temperature"
SENSOR_BOILER_WATER_TEMPERATURE = "boiler_water_temperature"
SENSOR_BURNER_STARTS = "burner_starts"
SENSOR_BURNER_OPERATION_HOURS = "burner_operation_hours"
SENSOR_MAX_RELATIVE_MODULATION_LEVEL = "max_relative_modulation_level"
SENSOR_RELATIVE_MODULATION_LEVEL = "relative_modulation_level"
SENSOR_DHW_TEMPERATURE = "dhw_temperature"
SENSOR_OUTSIDE_TEMPERATURE = "outside_temperature"
SENSOR_RETURN_WATER_TEMPERATURE = "return_water_temperature"
SENSOR_DHW_FLOW_RATE = "dhw_flow_rate"
SENSOR_CH2_FLOW_TEMPERATURE = "ch2_flow_temperature"
SENSOR_CONTROL_SETPOINT_2 = "control_setpoint_2"
SENSOR_EXHAUST_TEMPERATURE = "exhaust_temperature"
SENSOR_CH_PUMP_STARTS = "ch_pump_starts"
SENSOR_DHW_PUMP_VALVE_STARTS = "dhw_pump_valve_starts"
SENSOR_DHW_BURNER_STARTS = "dhw_burner_starts"
SENSOR_CH_PUMP_OPERATION_HOURS = "ch_pump_operation_hours"
SENSOR_DHW_PUMP_VALVE_OPERATION_HOURS = "dhw_pump_valve_operation_hours"
SENSOR_DHW_BURNER_OPERATION_HOURS = "dhw_burner_operation_hours"
SENSOR_OPENTHERM_VERSION_MASTER = "opentherm_version_master"
SENSOR_OPENTHERM_VERSION_SLAVE = "opentherm_version_slave"

@dataclass
class OpenThermGatewaySensorConfig:
    data_id: int
    data_type: str
    clear_on_timeout: bool = True

SENSOR_CONFIG = {
    SENSOR_CONTROL_SETPOINT: OpenThermGatewaySensorConfig(1, "F88"),
    SENSOR_MAX_RELATIVE_MODULATION_LEVEL: OpenThermGatewaySensorConfig(14, "F88"),
    SENSOR_ROOM_SETPOINT: OpenThermGatewaySensorConfig(16, "F88"),
    SENSOR_RELATIVE_MODULATION_LEVEL: OpenThermGatewaySensorConfig(17, "F88"),
    SENSOR_CENTRAL_HEATING_WATER_PRESSURE: OpenThermGatewaySensorConfig(18, "F88"),
    SENSOR_ROOM_TEMPERATURE: OpenThermGatewaySensorConfig(24, "F88"),
    SENSOR_BOILER_WATER_TEMPERATURE: OpenThermGatewaySensorConfig(25, "F88"),
    SENSOR_BURNER_STARTS: OpenThermGatewaySensorConfig(116, "U16", clear_on_timeout=False),
    SENSOR_BURNER_OPERATION_HOURS: OpenThermGatewaySensorConfig(120, "U16", clear_on_timeout=False),
    SENSOR_DHW_TEMPERATURE: OpenThermGatewaySensorConfig(26, "F88"),
    SENSOR_OUTSIDE_TEMPERATURE: OpenThermGatewaySensorConfig(27, "F88"),
    SENSOR_RETURN_WATER_TEMPERATURE: OpenThermGatewaySensorConfig(28, "F88"),
    SENSOR_DHW_FLOW_RATE: OpenThermGatewaySensorConfig(19, "F88"),
    SENSOR_CH2_FLOW_TEMPERATURE: OpenThermGatewaySensorConfig(31, "F88"),
    SENSOR_CONTROL_SETPOINT_2: OpenThermGatewaySensorConfig(8, "F88"),
    SENSOR_EXHAUST_TEMPERATURE: OpenThermGatewaySensorConfig(33, "S16"),
    SENSOR_CH_PUMP_STARTS: OpenThermGatewaySensorConfig(117, "U16", clear_on_timeout=False),
    SENSOR_DHW_PUMP_VALVE_STARTS: OpenThermGatewaySensorConfig(118, "U16", clear_on_timeout=False),
    SENSOR_DHW_BURNER_STARTS: OpenThermGatewaySensorConfig(119, "U16", clear_on_timeout=False),
    SENSOR_CH_PUMP_OPERATION_HOURS: OpenThermGatewaySensorConfig(121, "U16", clear_on_timeout=False),
    SENSOR_DHW_PUMP_VALVE_OPERATION_HOURS: OpenThermGatewaySensorConfig(122, "U16", clear_on_timeout=False),
    SENSOR_DHW_BURNER_OPERATION_HOURS: OpenThermGatewaySensorConfig(123, "U16", clear_on_timeout=False),
    SENSOR_OPENTHERM_VERSION_MASTER: OpenThermGatewaySensorConfig(124, "F88"),
    SENSOR_OPENTHERM_VERSION_SLAVE: OpenThermGatewaySensorConfig(125, "F88"),
}


CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(CONF_OTGW_ID): cv.use_id(OpenThermGateway),
    cv.Optional(SENSOR_CONTROL_SETPOINT): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_DHW_TEMPERATURE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_OUTSIDE_TEMPERATURE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_RETURN_WATER_TEMPERATURE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_DHW_FLOW_RATE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement='l/min',
        accuracy_decimals=2,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_CH2_FLOW_TEMPERATURE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_CONTROL_SETPOINT_2): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_EXHAUST_TEMPERATURE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=0,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_CH_PUMP_STARTS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional(SENSOR_DHW_PUMP_VALVE_STARTS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional(SENSOR_DHW_BURNER_STARTS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional(SENSOR_CH_PUMP_OPERATION_HOURS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_HOUR,
        accuracy_decimals=0,
        device_class=DEVICE_CLASS_DURATION,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional(SENSOR_DHW_PUMP_VALVE_OPERATION_HOURS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_HOUR,
        accuracy_decimals=0,
        device_class=DEVICE_CLASS_DURATION,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional(SENSOR_DHW_BURNER_OPERATION_HOURS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_HOUR,
        accuracy_decimals=0,
        device_class=DEVICE_CLASS_DURATION,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional(SENSOR_OPENTHERM_VERSION_MASTER): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=2,
        state_class=STATE_CLASS_MEASUREMENT,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
    ),
    cv.Optional(SENSOR_OPENTHERM_VERSION_SLAVE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=2,
        state_class=STATE_CLASS_MEASUREMENT,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
    ),
    cv.Optional(SENSOR_MAX_RELATIVE_MODULATION_LEVEL): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_PERCENT,
        accuracy_decimals=2,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_RELATIVE_MODULATION_LEVEL): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_PERCENT,
        accuracy_decimals=2,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_ROOM_SETPOINT): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
    ),
    cv.Optional(SENSOR_ROOM_TEMPERATURE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=2,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_CENTRAL_HEATING_WATER_PRESSURE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement='bar',
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_PRESSURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_BURNER_OPERATION_HOURS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_HOUR,
        accuracy_decimals=0,
        device_class=DEVICE_CLASS_DURATION,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional(SENSOR_BOILER_WATER_TEMPERATURE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=0,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_BURNER_STARTS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
})

async def to_code(config):
    parent = await cg.get_variable(config[CONF_OTGW_ID])

    for key, conf in config.items():
        if not isinstance(conf, dict):
            continue
        id = conf[CONF_ID]
        if id and id.type == sensor.Sensor:
            sens = await sensor.new_sensor(conf)
            await cg.register_component(sens, conf)
            sensorconfig = SENSOR_CONFIG[key]
            cg.add(sens.set_parent(parent))
            cg.add(sens.set_data_id(sensorconfig.data_id))
            cg.add(sens.set_data_type(cg.RawExpression(f"otgw::OpenThermDataType::{sensorconfig.data_type}")))
            cg.add(sens.set_clear_on_timeout(sensorconfig.clear_on_timeout))
