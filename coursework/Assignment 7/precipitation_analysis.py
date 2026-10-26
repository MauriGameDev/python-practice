
import os #os module to handle PATH flexibility for writing to the file

MIN_PRECIPITATION = 0.0

# Greatest monthly rainfall ever recorded: 366 inches, measured at
# Cherrapunji, Meghalaya, India, in July 1861 (Guinness World Records).
# Used as a generous upper bound since a reasonable "normal" range
# depends heavily on location.
MAX_PRECIPITATION = 366.0

# Name of the text file that stores the month names and precipitation amounts.
OUTPUT_FILE = 'precipitation.txt'


def main():
    # Create a list of the month names, January through December.
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    # Use the repetition operator to initialize the precipitation list with 0.0 for each month.
    precipitation = [0.0] * len(months)

    # Loop through the months and prompt the user for each month's precipitation.
    for i in range(len(months)):
        precipitation[i] = get_precipitation(months[i])

    # analyze the data using list methods and functions
    analyze_precipitation(precipitation, months)

    # Save each month name with its precipitation amount to a text file.
    path = write_precipitation_file(months, precipitation)
    print(f'Data saved to {path}')


"""
TODO - prompt the user to enter precipitation for the given month. Validate the input until a valid value is received.
       use try/except to capture ValueError, which can be resulted from text to float conversion.
"""
def get_precipitation(month):
    # Keep asking until the user enters a valid number.
    while True:
        try:
            rainfall = float(input(f'Enter the rainfall for {month}: '))

            # Check if rainfall is within the allowed range.
            if MIN_PRECIPITATION <= rainfall <= MAX_PRECIPITATION:
                return rainfall
            else:
                print(f'Invalid input. Please enter a value between {MIN_PRECIPITATION} and {MAX_PRECIPITATION}.')

        except ValueError:
            print(f'Invalid input. Please enter a value between {MIN_PRECIPITATION} and {MAX_PRECIPITATION}.')


"""
TODO - use list functions and methods to calculate annual precipitation total, average monthly precipitation, the highest
       preciptiation and month, and the lowest precipitation and month
"""
def analyze_precipitation(precipitation, months):
    # Calculate total rainfall.
    total = sum(precipitation)

    # Calculate average rainfall.
    average = total / len(precipitation)

    # Find highest and lowest rainfall.
    highest = max(precipitation)
    lowest = min(precipitation)

    # Find the months with highest and lowest rainfall.
    highest_month = months[precipitation.index(highest)]
    lowest_month = months[precipitation.index(lowest)]

    # Display the results.
    print(f'Total rainfall: {total:.2f}')
    print(f'Average rainfall: {average:.2f}')
    print(f'Highest rainfall: {highest_month} {highest:.1f}')
    print(f'Lowest rainfall: {lowest_month} {lowest:.1f}')


"""
TODO - write the month and its preciptiation to the given file, in a format of for example
       January,3.25
       use try/except to capture OSError that can be raised in file writing (return None)
"""
def write_precipitation_file(months, precipitation, filename=OUTPUT_FILE):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    try:
        with open(path, 'w') as output_file:
            # Write each month and its rainfall to the file.
            for i in range(len(months)):
                output_file.write(f'{months[i]},{precipitation[i]}\n')

    except OSError as error:
        print(f"Could not save the data to '{path}': {error}")
        return None

    return path


# Call the main function only if this file is run directly.
if __name__ == '__main__':
    main()
