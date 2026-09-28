"""Convert temperatures between Fahrenheit and Celsius
and validate the user's input."""

# named constants
ABSOLUTE_ZERO_F = -459.67
ABSOLUTE_ZERO_C = -273.15

# get input from the user
temperature = float(input('Enter the temperature you want to convert: '))
temperature_type = input(
    'Enter the type of temperature (F for Fahrenheit, C for Celsius): '
)

# determine the type and validate the temperature
if temperature_type == 'F':
    if temperature >= ABSOLUTE_ZERO_F:
        celsius = (temperature - 32) * 5 / 9
        print(f'The temperature in Celsius is: {celsius:.2f}')
    else:
        print('Invalid temperature. Please enter a temperature above absolute zero.')

elif temperature_type == 'C':
    if temperature >= ABSOLUTE_ZERO_C:
        fahrenheit = (temperature * 9 / 5) + 32
        print(f'The temperature in Fahrenheit is: {fahrenheit:.2f}')
    else:
        print('Invalid temperature. Please enter a temperature above absolute zero.')

else:
    print("Invalid temperature type. Please enter 'F' for Fahrenheit or 'C' for Celsius.")