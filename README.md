# OpenTherm Gateway integration for ESPHome

This plugin intends to parse the serial communication as provided by an OpenTherm Gateway (OTGW). The OTGW project can be found here: https://otgw.tclcode.com/

The main entity is the climate integration which allows viewing and controlling of the room setpoint.

For other sensors, only a subset of OTGW messages are parsed. New sensors can be added fairly easily by modifying `otgw/sensor/__init__.py`. Feel free to make a pull-request.

## Example Configuration

```yaml
external_components:
  - source: github://mvdnes/esphome-otgw

uart:
  # Serial for OTGW PIC
  - id: uart_otgw
    baud_rate: 9600
    tx_pin: GPIO1
    rx_pin: GPIO3
    data_bits: 8
    parity: NONE
    stop_bits: 1

otgw:
  uart_id: uart_otgw

climate:
  - platform: otgw
    room_thermostat:
      name: Thermostat

sensor:
  - platform: otgw
    status:
      name: Master and Slave status
    slave_config_member_id_code:
      name: Slave Config / Member ID
    asf_flags:
      name: Application-specific fault
    rbp_flags:
      name: Remote-parameter flags
    tr_override:
      name: Remote override room setpoint
    tsp:
      name: Number of TSPs
    fhb_size:
      name: Size of Fault-History-Buffer supported by slave
    fhb_index_value:
      name: Index number / Value of referred-to fault-history buffer entry
    max_capacity_min_mod_level:
      name: Maximum boiler capacity (kW) / Minimum boiler modulation level(%)
    rel_mod_level:
      name: Relative Modulation Level
    ch_pressure:
      name: CH water pressure
    dhw_flow_rate:
      name: DHW flow rate
    t_boiler:
      name: Boiler water temperature
    t_dhw:
      name: DHW temperature
    t_outside:
      name: Outside temperature
    t_return:
      name: Return water temperature
    t_solar_storage:
      name: Solar storage temperature
    t_solar_collector:
      name: Solar collector temperature
    t_flow_ch2:
      name: Flow water temperature CH2
    t_dhw2:
      name: DHW2 temperature
    t_exhaust:
      name: Exhaust temperature
    t_heat_exchanger:
      name: Boiler heat exchanger temperature
    fan_speed:
      name: Boiler fan speed and setpoint
    flame_current:
      name: Electrical current through burner flame
    t_room_ch2:
      name: Room temperature for 2nd CH circuit
    relative_humidity:
      name: Relative Humidity
    t_dhw_set_bounds:
      name: DHW setpoint upper & lower bounds for adjustment
    max_t_set_bounds:
      name: Max CH water setpoint upper & lower bounds for adjustment
    hc_ratio_bounds:
      name: OTC heat curve ratio upper & lower bounds for adjustment
    remote_param4_bounds:
      name: Remote parameter 4 boundaries
    remote_param5_bounds:
      name: Remote parameter 5 boundaries
    remote_param6_bounds:
      name: Remote parameter 6 boundaries
    remote_param7_bounds:
      name: Remote parameter 7 boundaries
    remote_param8_bounds:
      name: Remote parameter 8 boundaries
    status_vh:
      name: Status Ventilation/Heat recovery
    asf_fault_code_vh:
      name: Application-specific Fault Flags/Code V/H
    diagnostic_code_vh:
      name: Diagnostic code V/H
    config_member_id_vh:
      name: Config/Member ID V/H
    opentherm_version_vh:
      name: OpenTherm version V/H
    version_type_vh:
      name: Product version & type V/H
    relative_ventilation:
      name: Relative ventilation
    supply_inlet_temperature:
      name: Supply inlet temperature
    supply_outlet_temperature:
      name: Supply outlet temperature
    exhaust_inlet_temperature:
      name: Exhaust inlet temperature
    exhaust_outlet_temperature:
      name: Exhaust outlet temperature
    exhaust_fan_speed:
      name: Actual exhaust fan speed
    supply_fan_speed:
      name: Actual supply fan speed
    remote_parameter_setting_vh:
      name: Remote Parameter Setting V/H
    tsp_number_vh:
      name: TSP Number V/H
    fault_buffer_size_vh:
      name: Fault Buffer Size V/H
    fault_buffer_entry_vh:
      name: Fault Buffer Entry V/H
    rf_strength_battery_level:
      name: RF strength and battery level
    operating_mode_hc1_hc2_dhw:
      name: Operating Mode HC1, HC2/ DHW
    room_remote_override_function:
      name: Function of manual and program changes in master and remote room setpoint.
    solar_storage_master:
      name: Solar Storage Master mode
    solar_storage_asf_flags:
      name: Solar Storage Application-specific flags and OEM fault
    solar_storage_slave_config_member_id_code:
      name: Solar Storage Slave Config / Member ID
    solar_storage_version_type:
      name: Solar Storage product version number and type
    solar_storage_tsp:
      name: Solar Storage Number of Transparent-Slave-Parameters supported
    solar_storage_fhb_size:
      name: Solar Storage Size of Fault-History-Buffer supported by slave
    solar_storage_fhb_index_value:
      name: Solar Storage Index number / Value of referred-to fault-history buffer entry
    electricity_producer_starts:
      name: Electricity producer starts
    electricity_producer_hours:
      name: Electricity producer hours
    electricity_production:
      name: Electricity production
    cumulative_electricity_production:
      name: Cumulative Electricity production
    oem_diagnostic_code:
      name: OEM-specific diagnostic/service code
    opentherm_version_master:
      name: Master Version OpenTherm Protocol Specification
    opentherm_version_slave:
      name: Slave Version OpenTherm Protocol Specification
    master_version:
      name: Master product version number and type
    slave_version:
      name: Slave product version number and type
    remeha_service_message:
      name: Remeha Servicemessage
    remeha_detection_connected_scu:
      name: Remeha detection connected SCU’s

binary_sensor:
  - platform: otgw
    fault_indication:
      name: Fault Indication
    ch_active:
      name: Central Heating State
    dhw_active:
      name: Domestic Hot Water State
    flame_status:
      name: Flame Status

text_sensor:
  - platform: otgw
    version:
      name: OTGW version
```

Optional additional configuration to ensure a reset of the OTGW PIC when ESPHome is reloaded:

```yaml
esphome:
  # ...other config options...
  on_boot:
    # Reset the OTGW PIC
    # This ensures the debug output of the esp on the serial output does not confuse the PIC
    priority: 600
    then:
      - output.turn_off: pic_reset_n
      - delay: 100ms
      - output.turn_on: pic_reset_n

output:
  # Reset line of the OTGW PIC
  - platform: gpio
    pin:
      number: GPIO14
      mode:
        output: true
        open_drain: true
    id: pic_reset_n
```

