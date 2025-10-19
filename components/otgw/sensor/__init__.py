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


SENSOR_TR_OVERRIDE = "tr_override"
SENSOR_REL_MOD_LEVEL = "rel_mod_level"
SENSOR_CH_PRESSURE = "ch_pressure"
SENSOR_DHW_FLOW_RATE = "dhw_flow_rate"
SENSOR_T_BOILER = "t_boiler"
SENSOR_T_DHW = "t_dhw"
SENSOR_T_OUTSIDE = "t_outside"
SENSOR_T_RETURN = "t_return"
SENSOR_T_SOLAR_STORAGE = "t_solar_storage"
SENSOR_T_SOLAR_COLLECTOR = "t_solar_collector"
SENSOR_T_FLOW_CH2 = "t_flow_ch2"
SENSOR_T_DHW2 = "t_dhw2"
SENSOR_T_EXHAUST = "t_exhaust"
SENSOR_T_HEAT_EXCHANGER = "t_heat_exchanger"
SENSOR_FLAME_CURRENT = "flame_current"
SENSOR_T_ROOM_CH2 = "t_room_ch2"
SENSOR_FAN_SPEED = "fan_speed"
SENSOR_SUPPLY_INLET_TEMPERATURE = "supply_inlet_temperature"
SENSOR_SUPPLY_OUTLET_TEMPERATURE = "supply_outlet_temperature"
SENSOR_EXHAUST_INLET_TEMPERATURE = "exhaust_inlet_temperature"
SENSOR_EXHAUST_OUTLET_TEMPERATURE = "exhaust_outlet_temperature"
SENSOR_EXHAUST_FAN_SPEED = "exhaust_fan_speed"
SENSOR_SUPPLY_FAN_SPEED = "supply_fan_speed"
SENSOR_ELECTRICITY_PRODUCER_STARTS = "electricity_producer_starts"
SENSOR_ELECTRICITY_PRODUCER_HOURS = "electricity_producer_hours"
SENSOR_ELECTRICITY_PRODUCTION = "electricity_production"
SENSOR_CUMULATIVE_ELECTRICITY_PRODUCTION = "cumulative_electricity_production"
SENSOR_OEM_DIAGNOSTIC_CODE = "oem_diagnostic_code"
SENSOR_OPENTHERM_VERSION_MASTER = "opentherm_version_master"
SENSOR_OPENTHERM_VERSION_SLAVE = "opentherm_version_slave"
SENSOR_STATUS = "status"
SENSOR_SLAVE_CONFIG_MEMBER_ID = "slave_config_member_id_code"
SENSOR_ASF_FLAGS = "asf_flags"
SENSOR_RBP_FLAGS = "rbp_flags"
SENSOR_TSP = "tsp"
SENSOR_FHB_SIZE = "fhb_size"
SENSOR_FHB_INDEX_VALUE = "fhb_index_value"
SENSOR_MAX_CAPACITY_MIN_MOD_LEVEL = "max_capacity_min_mod_level"
SENSOR_RELATIVE_HUMIDITY = "relative_humidity"
SENSOR_T_DHW_SET_BOUNDS = "t_dhw_set_bounds"
SENSOR_MAX_T_SET_BOUNDS = "max_t_set_bounds"
SENSOR_HC_RATIO_BOUNDS = "hc_ratio_bounds"
SENSOR_REMOTE_PARAM4_BOUNDS = "remote_param4_bounds"
SENSOR_REMOTE_PARAM5_BOUNDS = "remote_param5_bounds"
SENSOR_REMOTE_PARAM6_BOUNDS = "remote_param6_bounds"
SENSOR_REMOTE_PARAM7_BOUNDS = "remote_param7_bounds"
SENSOR_REMOTE_PARAM8_BOUNDS = "remote_param8_bounds"
SENSOR_STATUS_VH = "status_vh"
SENSOR_ASF_FAULT_CODE_VH = "asf_fault_code_vh"
SENSOR_DIAGNOSTIC_CODE_VH = "diagnostic_code_vh"
SENSOR_CONFIG_MEMBER_ID_VH = "config_member_id_vh"
SENSOR_OPENTHERM_VERSION_VH = "opentherm_version_vh"
SENSOR_VERSION_TYPE_VH = "version_type_vh"
SENSOR_RELATIVE_VENTILATION = "relative_ventilation"
SENSOR_REMOTE_PARAMETER_SETTING_VH = "remote_parameter_setting_vh"
SENSOR_TSP_NUMBER_VH = "tsp_number_vh"
SENSOR_FAULT_BUFFER_SIZE_VH = "fault_buffer_size_vh"
SENSOR_FAULT_BUFFER_ENTRY_VH = "fault_buffer_entry_vh"
SENSOR_RF_STRENGTH_BATTERY_LEVEL = "rf_strength_battery_level"
SENSOR_OPERATING_MODE = "operating_mode_hc1_hc2_dhw"
SENSOR_ROOM_REMOTE_OVERRIDE_FUNCTION = "room_remote_override_function"
SENSOR_SOLAR_STORAGE_MASTER = "solar_storage_master"
SENSOR_SOLAR_STORAGE_ASF_FLAGS = "solar_storage_asf_flags"
SENSOR_SOLAR_STORAGE_SLAVE_CONFIG_MEMBER_ID = "solar_storage_slave_config_member_id_code"
SENSOR_SOLAR_STORAGE_VERSION_TYPE = "solar_storage_version_type"
SENSOR_SOLAR_STORAGE_TSP = "solar_storage_tsp"
SENSOR_SOLAR_STORAGE_FHB_SIZE = "solar_storage_fhb_size"
SENSOR_SOLAR_STORAGE_FHB_INDEX_VALUE = "solar_storage_fhb_index_value"
SENSOR_MASTER_VERSION = "master_version"
SENSOR_SLAVE_VERSION = "slave_version"
SENSOR_REMEHA_SERVICE_MESSAGE = "remeha_service_message"
SENSOR_REMEHA_DETECTION_CONNECTED_SCU = "remeha_detection_connected_scu"

@dataclass
class OpenThermGatewaySensorConfig:
    data_id: int
    data_type: str
    clear_on_timeout: bool = True

SENSOR_CONFIG = {
    SENSOR_STATUS: OpenThermGatewaySensorConfig(0, "U16"),
    SENSOR_SLAVE_CONFIG_MEMBER_ID: OpenThermGatewaySensorConfig(3, "U16"),
    SENSOR_ASF_FLAGS: OpenThermGatewaySensorConfig(5, "U16"),
    SENSOR_RBP_FLAGS: OpenThermGatewaySensorConfig(6, "U16"),
    SENSOR_TR_OVERRIDE: OpenThermGatewaySensorConfig(9, "F88"),
    SENSOR_TSP: OpenThermGatewaySensorConfig(10, "U16"),
    SENSOR_FHB_SIZE: OpenThermGatewaySensorConfig(12, "U16"),
    SENSOR_FHB_INDEX_VALUE: OpenThermGatewaySensorConfig(13, "U16"),
    SENSOR_MAX_CAPACITY_MIN_MOD_LEVEL: OpenThermGatewaySensorConfig(15, "U16"),
    SENSOR_REL_MOD_LEVEL: OpenThermGatewaySensorConfig(17, "F88"),
    SENSOR_CH_PRESSURE: OpenThermGatewaySensorConfig(18, "F88"),
    SENSOR_DHW_FLOW_RATE: OpenThermGatewaySensorConfig(19, "F88"),
    SENSOR_T_BOILER: OpenThermGatewaySensorConfig(25, "F88"),
    SENSOR_T_DHW: OpenThermGatewaySensorConfig(26, "F88"),
    SENSOR_T_OUTSIDE: OpenThermGatewaySensorConfig(27, "F88"),
    SENSOR_T_RETURN: OpenThermGatewaySensorConfig(28, "F88"),
    SENSOR_T_SOLAR_STORAGE: OpenThermGatewaySensorConfig(29, "F88"),
    SENSOR_T_SOLAR_COLLECTOR: OpenThermGatewaySensorConfig(30, "S16"),
    SENSOR_T_FLOW_CH2: OpenThermGatewaySensorConfig(31, "F88"),
    SENSOR_T_DHW2: OpenThermGatewaySensorConfig(32, "F88"),
    SENSOR_T_EXHAUST: OpenThermGatewaySensorConfig(33, "S16"),
    SENSOR_T_HEAT_EXCHANGER: OpenThermGatewaySensorConfig(34, "F88"),
    SENSOR_FAN_SPEED: OpenThermGatewaySensorConfig(35, "U16"),
    SENSOR_FLAME_CURRENT: OpenThermGatewaySensorConfig(36, "F88"),
    SENSOR_T_ROOM_CH2: OpenThermGatewaySensorConfig(37, "F88"),
    SENSOR_RELATIVE_HUMIDITY: OpenThermGatewaySensorConfig(38, "U16"),
    SENSOR_T_DHW_SET_BOUNDS: OpenThermGatewaySensorConfig(48, "U16"),
    SENSOR_MAX_T_SET_BOUNDS: OpenThermGatewaySensorConfig(49, "U16"),
    SENSOR_HC_RATIO_BOUNDS: OpenThermGatewaySensorConfig(50, "U16"),
    SENSOR_REMOTE_PARAM4_BOUNDS: OpenThermGatewaySensorConfig(51, "U16"),
    SENSOR_REMOTE_PARAM5_BOUNDS: OpenThermGatewaySensorConfig(52, "U16"),
    SENSOR_REMOTE_PARAM6_BOUNDS: OpenThermGatewaySensorConfig(53, "U16"),
    SENSOR_REMOTE_PARAM7_BOUNDS: OpenThermGatewaySensorConfig(54, "U16"),
    SENSOR_REMOTE_PARAM8_BOUNDS: OpenThermGatewaySensorConfig(55, "U16"),
    SENSOR_STATUS_VH: OpenThermGatewaySensorConfig(70, "U16"),
    SENSOR_ASF_FAULT_CODE_VH: OpenThermGatewaySensorConfig(72, "U16"),
    SENSOR_DIAGNOSTIC_CODE_VH: OpenThermGatewaySensorConfig(73, "U16"),
    SENSOR_CONFIG_MEMBER_ID_VH: OpenThermGatewaySensorConfig(74, "U16"),
    SENSOR_OPENTHERM_VERSION_VH: OpenThermGatewaySensorConfig(75, "F88"),
    SENSOR_VERSION_TYPE_VH: OpenThermGatewaySensorConfig(76, "U16"),
    SENSOR_RELATIVE_VENTILATION: OpenThermGatewaySensorConfig(77, "U16"),
    SENSOR_SUPPLY_INLET_TEMPERATURE: OpenThermGatewaySensorConfig(80, "F88"),
    SENSOR_SUPPLY_OUTLET_TEMPERATURE: OpenThermGatewaySensorConfig(81, "F88"),
    SENSOR_EXHAUST_INLET_TEMPERATURE: OpenThermGatewaySensorConfig(82, "F88"),
    SENSOR_EXHAUST_OUTLET_TEMPERATURE: OpenThermGatewaySensorConfig(83, "F88"),
    SENSOR_EXHAUST_FAN_SPEED: OpenThermGatewaySensorConfig(84, "U16", clear_on_timeout=False),
    SENSOR_SUPPLY_FAN_SPEED: OpenThermGatewaySensorConfig(85, "U16", clear_on_timeout=False),
    SENSOR_REMOTE_PARAMETER_SETTING_VH: OpenThermGatewaySensorConfig(86, "U16"),
    SENSOR_TSP_NUMBER_VH: OpenThermGatewaySensorConfig(88, "U16"),
    SENSOR_FAULT_BUFFER_SIZE_VH: OpenThermGatewaySensorConfig(90, "U16"),
    SENSOR_FAULT_BUFFER_ENTRY_VH: OpenThermGatewaySensorConfig(91, "U16"),
    SENSOR_RF_STRENGTH_BATTERY_LEVEL: OpenThermGatewaySensorConfig(98, "U16"),
    SENSOR_OPERATING_MODE: OpenThermGatewaySensorConfig(99, "U16"),
    SENSOR_ROOM_REMOTE_OVERRIDE_FUNCTION: OpenThermGatewaySensorConfig(100, "U16"),
    SENSOR_SOLAR_STORAGE_MASTER: OpenThermGatewaySensorConfig(101, "U16"),
    SENSOR_SOLAR_STORAGE_ASF_FLAGS: OpenThermGatewaySensorConfig(102, "U16"),
    SENSOR_SOLAR_STORAGE_SLAVE_CONFIG_MEMBER_ID: OpenThermGatewaySensorConfig(103, "U16"),
    SENSOR_SOLAR_STORAGE_VERSION_TYPE: OpenThermGatewaySensorConfig(104, "U16"),
    SENSOR_SOLAR_STORAGE_TSP: OpenThermGatewaySensorConfig(105, "U16"),
    SENSOR_SOLAR_STORAGE_FHB_SIZE: OpenThermGatewaySensorConfig(107, "U16"),
    SENSOR_SOLAR_STORAGE_FHB_INDEX_VALUE: OpenThermGatewaySensorConfig(108, "U16"),
    SENSOR_ELECTRICITY_PRODUCER_STARTS: OpenThermGatewaySensorConfig(109, "U16", clear_on_timeout=False),
    SENSOR_ELECTRICITY_PRODUCER_HOURS: OpenThermGatewaySensorConfig(110, "U16", clear_on_timeout=False),
    SENSOR_ELECTRICITY_PRODUCTION: OpenThermGatewaySensorConfig(111, "U16", clear_on_timeout=False),
    SENSOR_CUMULATIVE_ELECTRICITY_PRODUCTION: OpenThermGatewaySensorConfig(112, "U16", clear_on_timeout=False),
    SENSOR_OEM_DIAGNOSTIC_CODE: OpenThermGatewaySensorConfig(115, "U16", clear_on_timeout=False),
    SENSOR_OPENTHERM_VERSION_MASTER: OpenThermGatewaySensorConfig(124, "F88"),
    SENSOR_OPENTHERM_VERSION_SLAVE: OpenThermGatewaySensorConfig(125, "F88"),
    SENSOR_MASTER_VERSION: OpenThermGatewaySensorConfig(126, "U16"),
    SENSOR_SLAVE_VERSION: OpenThermGatewaySensorConfig(127, "U16"),
    SENSOR_REMEHA_SERVICE_MESSAGE: OpenThermGatewaySensorConfig(132, "U16"),
    SENSOR_REMEHA_DETECTION_CONNECTED_SCU: OpenThermGatewaySensorConfig(133, "U16"),
}


CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(CONF_OTGW_ID): cv.use_id(OpenThermGateway),
    cv.Optional(SENSOR_STATUS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_SLAVE_CONFIG_MEMBER_ID): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_ASF_FLAGS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_RBP_FLAGS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_TR_OVERRIDE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_TSP): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_FHB_SIZE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_FHB_INDEX_VALUE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_MAX_CAPACITY_MIN_MOD_LEVEL): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_REL_MOD_LEVEL): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_PERCENT,
        accuracy_decimals=2,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_CH_PRESSURE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement='bar',
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_PRESSURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_DHW_FLOW_RATE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement='l/min',
        accuracy_decimals=2,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_T_BOILER): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_T_DHW): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_T_OUTSIDE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_T_RETURN): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_T_SOLAR_STORAGE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_T_SOLAR_COLLECTOR): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=0,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_T_FLOW_CH2): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_T_DHW2): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_T_EXHAUST): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=0,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_FAN_SPEED): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement='rpm',
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_T_HEAT_EXCHANGER): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_FLAME_CURRENT): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement='µA',
        accuracy_decimals=1,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_T_ROOM_CH2): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_RELATIVE_HUMIDITY): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_PERCENT,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_T_DHW_SET_BOUNDS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_MAX_T_SET_BOUNDS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_HC_RATIO_BOUNDS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_REMOTE_PARAM4_BOUNDS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_REMOTE_PARAM5_BOUNDS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_REMOTE_PARAM6_BOUNDS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_REMOTE_PARAM7_BOUNDS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_REMOTE_PARAM8_BOUNDS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_STATUS_VH): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_ASF_FAULT_CODE_VH): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_DIAGNOSTIC_CODE_VH): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_CONFIG_MEMBER_ID_VH): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_OPENTHERM_VERSION_VH): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=2,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_VERSION_TYPE_VH): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_RELATIVE_VENTILATION): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_PERCENT,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_SUPPLY_INLET_TEMPERATURE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_SUPPLY_OUTLET_TEMPERATURE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_EXHAUST_INLET_TEMPERATURE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_EXHAUST_OUTLET_TEMPERATURE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_EXHAUST_FAN_SPEED): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement='rpm',
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_SUPPLY_FAN_SPEED): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement='rpm',
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_REMOTE_PARAMETER_SETTING_VH): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_TSP_NUMBER_VH): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_FAULT_BUFFER_SIZE_VH): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_FAULT_BUFFER_ENTRY_VH): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_RF_STRENGTH_BATTERY_LEVEL): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_OPERATING_MODE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_ROOM_REMOTE_OVERRIDE_FUNCTION): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_SOLAR_STORAGE_MASTER): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_SOLAR_STORAGE_ASF_FLAGS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_SOLAR_STORAGE_SLAVE_CONFIG_MEMBER_ID): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_SOLAR_STORAGE_VERSION_TYPE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_SOLAR_STORAGE_TSP): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_SOLAR_STORAGE_FHB_SIZE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_SOLAR_STORAGE_FHB_INDEX_VALUE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_ELECTRICITY_PRODUCER_STARTS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional(SENSOR_ELECTRICITY_PRODUCER_HOURS): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_HOUR,
        accuracy_decimals=0,
        device_class=DEVICE_CLASS_DURATION,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional(SENSOR_ELECTRICITY_PRODUCTION): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional(SENSOR_CUMULATIVE_ELECTRICITY_PRODUCTION): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional(SENSOR_OEM_DIAGNOSTIC_CODE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        state_class=STATE_CLASS_MEASUREMENT,
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
    cv.Optional(SENSOR_MASTER_VERSION): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_SLAVE_VERSION): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_REMEHA_SERVICE_MESSAGE): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(SENSOR_REMEHA_DETECTION_CONNECTED_SCU): sensor.sensor_schema(
        OpenThermGatewaySensor,
        unit_of_measurement=UNIT_EMPTY,
        accuracy_decimals=0,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        state_class=STATE_CLASS_MEASUREMENT,
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
