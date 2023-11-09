# Function that converts Fahrenheit in Celcius
def convert_to_fahrenheit(temperature, scale):
    if scale.lower() == 'c':
        return (temperature * 9/5) + 32
    else:
        return temperature

# Function to calculate the temperature
def calculation_windchill(temperature, speed):
    windchill = 35.74 + 0.6215 * temperature - 35.75 * (speed ** 0.16) + 0.4275 * temperature * (speed ** 0.16)
    return windchill
        
# Ask the user fot the temperature F or C
temperature_str = input("What is the temperature? ")
scale = input("Fahrenheit or Celsius (F/C)? ")

temperature_value = float(temperature_str)

#Converts to Fahrenheit if the temperature is Celcius
if scale.lower() == 'c':
    temperature_fahrenheit = convert_to_fahrenheit(temperature_value, scale)
else:
    temperature_fahrenheit = temperature_value

# Now the loop for calculate the speed
print(f"At temperature {temperature_fahrenheit} °F:")
for speed in range(5, 61, 5):
    windchill = calculation_windchill(temperature_fahrenheit, speed)
    print(f"At wind speed {speed} mph, the windchill is {windchill:.2f} °F")
