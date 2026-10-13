# Celsius Conversion Program

# Named constant
ABSOLUTE_ZERO = -273.15

# Get and validate the Celsius temperature
celsius = int(input('Enter a Celsius temperature: '))

while celsius < ABSOLUTE_ZERO:
    print('Error: temperature cannot be below absolute zero.')
    celsius = int(input('Enter a Celsius temperature: '))

# Display column headings
print(f'{"Celsius":<12}{"Fahrenheit":<12}')

# Convert temperatures from 0 up to the entered temperature
if celsius >= 0:
    for degree in range(0, celsius + 1):
        fahrenheit = (degree * 9 / 5) + 32
        print(f'{degree:<12}{fahrenheit:<12.2f}')

else:
    for degree in range(0, celsius - 1, -1):
        fahrenheit = (degree * 9 / 5) + 32
        print(f'{degree:<12}{fahrenheit:<12.2f}')