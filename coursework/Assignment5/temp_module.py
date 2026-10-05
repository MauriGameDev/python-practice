#TODO: define Global Constants
ABSOLUTE_ZERO_F = -459.67
ABSOLUTE_ZERO_C = -273.15

def main():
    temperature_type = get_temperature_type()
    temperature = get_temperature(temperature_type)
    display_conversion(temperature_type, temperature)

# TODO: complete this function which prompt user for the temperature type (C or F) until a valid input is received.
def get_temperature_type():
    temp = str(input("Enter the type of temperature (F for Fahrenheit, C for Celsius): ")).upper()
    if temp == "C":
        get_temperature("C")
    elif temp == "F":
        get_temperature("F")
    else:
        print("Invalid temperature type. Please enter (F) Fahrenheit or (C) Celsius.")
    return temp

# TODO: complete this function which prompt user for the temperature until a valid value is received.
def get_temperature(temperature_type):
    temperature = float(input("Enter the temperature you want to convert: "))

    if temperature_type == "F":
        while temperature < ABSOLUTE_ZERO_F:
            print(f"Invalid temperature. Please enter a temperature above absolute zero {ABSOLUTE_ZERO_F}")

            temperature = float(input("Enter the temperature you want to convert: "))
    else:
        while temperature < ABSOLUTE_ZERO_C:
            print(f"Invalid temperature. Please enter a temperature above absolute zero {ABSOLUTE_ZERO_C}.")

            temperature = float(input("Enter the temperature to convert: "))
    return temperature



        

   

# TODO: complete this function which perform conversion based on the type
def display_conversion(temperature_type, temperature):
    pass


if __name__ == "__main__":
    main()