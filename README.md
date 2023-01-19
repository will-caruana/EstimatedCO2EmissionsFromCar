# EstimatedCO2EmissionsFromCar
This program used OBD II PIDs to calculate the amount of CO2 emissions the car is producing.

To run this you need to have odb libary install which you can do with this command: pip install obd

OBD-II PIDs (parameter identification codes) are used to retrieve various data from a vehicle's engine control unit (ECU), including information about the vehicle's emissions. However, the information available through OBD-II PIDs is limited and may not be sufficient to accurately calculate the exact amount of CO2 emissions produced by a vehicle.

Some OBD-II PIDs can provide data that can be used to estimate CO2 emissions, such as the vehicle's speed, engine RPM, and fuel consumption. However, these data points alone may not provide a precise measurement of CO2 emissions, as other factors such as the engine's efficiency and the composition of the fuel being used also have an impact on emissions.

Additionally, the information provided by OBD-II PIDs is often a calculated value, not a direct measurement, meaning that it could also be affected by inaccuracies in the vehicle's sensors or the ECU's calculations.

In order to accurately measure the CO2 emissions produced by a vehicle, it would be necessary to use specialized equipment and perform tests in a controlled environment. Many countries have regulations and organizations that set standards for measuring CO2 emissions, such as the European Union's New European Driving Cycle (NEDC) and the United States Environmental Protection Agency (EPA).

This script uses the data obtained from OBD-II PIDs to estimate the CO2 emissions, it takes the fuel consumption, speed, and RPM of the car and makes the calculation to estimate CO2 emissions.
