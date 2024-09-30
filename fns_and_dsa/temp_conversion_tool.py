FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature = input("Enter the temperature to convert: ")

 # Check if the temperature is a valid number (int, float, or numeric string)
if isinstance(temperature, (int, float)) or (isinstance(temperature, str) and temperature.replace('.', '', 1).isdigit()):
    temperature = float(temperature)  # Convert to float
    
else:
        # Raise a ValueError with the custom message
    raise ValueError("Invalid temperature. Please enter a numeric value.")




temperature_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

def convert_to_celsius(temperature):
    return (temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(temperature):
    return (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if temperature_unit == "C":
    convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")

elif temperature_unit == "F":
    convert_to_celsius(temperature)
    print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")

