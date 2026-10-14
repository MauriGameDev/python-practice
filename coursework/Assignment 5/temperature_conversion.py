#TODO: define Global Constants
ABSOLUTE_ZERO_F = -459.67
ABSOLUTE_ZERO_C = -273.15

def main():
    temperature_type = get_temperature_type()
    temperature = get_temperature(temperature_type)
    display_conversion(temperature_type, temperature)

# TODO: complete this function which prompt user for the temperature type (C or F) until a valid input is received.
def get_temperature_type():
    while (temp := input("Enter the type of temperature (F) for Fahrenheit, (C) for Celsius: ").upper()) != "F" and temp != "C":
        print("Invalid temperature type. Please enter (F) for Fahrenheit or (C) for Celsius.")
    return temp
   


# TODO: complete this function which prompt user for the temperature until a valid value is received.
def get_temperature(temperature_type):
    if temperature_type == "F":
        while (temperature := float(input("Enter the temperature you want to convert: "))) < ABSOLUTE_ZERO_F:
            print(f"Invalid temperature. Please enter a temperature above absolute zero {ABSOLUTE_ZERO_F}")
    else:
        while (temperature := float(input("Enter the temperature you want to convert: "))) < ABSOLUTE_ZERO_C:
            print(f"Invalid temperature. Please enter a temperature above absolute zero {ABSOLUTE_ZERO_C}")
    return temperature
            
            
# TODO: complete this function which perform conversion based on the type
def display_conversion(temperature_type, temperature):
    if temperature_type == "F":
        converted_temperature = (temperature - 32) * 5/9
        print(f"The temperature in Celsius is: {converted_temperature:.2f}")
    
    else:
        converted_temperature = (temperature * 9/5) + 32
        print(f"The temperature in Fahreheit is: {converted_temperature:.2f}")


if __name__ == "__main__":
    main()