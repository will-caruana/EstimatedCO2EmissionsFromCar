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

# Estimate CO2 emissions
emissions = (fuel_consumption * 3600) / (speed / 3.6)
print("Estimated CO2 emissions: {:.2f} g/km".format(emissions))
