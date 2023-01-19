import obd

# Connect to the OBD-II adapter
connection = obd.OBD()

# Get vehicle speed
speed_cmd = obd.commands.SPEED
speed_response = connection.query(speed_cmd)
speed = speed_response.value.magnitude

# Get engine RPM
rpm_cmd = obd.commands.RPM
rpm_response = connection.query(rpm_cmd)
rpm = rpm_response.value.magnitude

# Get fuel consumption
fuel_cmd = obd.commands.FUEL_RATE
fuel_response = connection.query(fuel_cmd)
fuel_consumption = fuel_response.value.magnitude

# Get temperature
temp_cmd = obd.commands.AMBIANT_AIR_TEMP
temp_response = connection.query(temp_cmd)
temperature = temp_response.value.magnitude

# Get pressure
pressure_cmd = obd.commands.BAROMETRIC_PRESSURE
pressure_response = connection.query(pressure_cmd)
pressure = pressure_response.value.magnitude

# Estimate CO2 emissions
co2_emission = (fuel_consumption * (652 + (1740*(273+temperature)/273*(pressure/1013.25)**0.288)))/(speed/3.6)
print("Estimated CO2 emissions: {:.2f} g/km".format(co2_emission))
