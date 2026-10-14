# Star Pattern Program

ROWS = 7

# Outer loop controls the rows
for row in range(ROWS, 0, -1):

    # Inner loop controls the stars in each row
    for column in range(row):
        print('*', end='')

    # Move to the next line
    print()