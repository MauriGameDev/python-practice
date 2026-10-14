# Fixed-income Investment Revenue Program

MONTHS_IN_YEAR = 12

# Get and validate the monthly investment
while (monthly_investment := float(
        input('Enter a monthly investment amount: '))) <= 0:

    print('Error: investment must be a positive number')

# Get and validate the yearly interest rate
while (yearly_interest_rate := float(
        input('Enter a yearly interest rate: '))) <= 0:

    print('Error: yearly interest rate must be a positive number')

# Get and validate the investment period
while (investment_years := int(
        input('Enter how many years to invest: '))) <= 0:

    print('Error: investment period must be a positive number of years')

# Calculate the monthly interest rate
monthly_interest_rate = (
    yearly_interest_rate / 100 / MONTHS_IN_YEAR
)

# Calculate the number of months
total_months = investment_years * MONTHS_IN_YEAR

# Initialize the investment revenue
investment_revenue = 0

# Calculate the investment month by month
for month in range(1, total_months + 1):

    investment_revenue = (
        investment_revenue + monthly_investment
    ) * (1 + monthly_interest_rate)

    print(f'Month {month} revenue: {investment_revenue}')

# Display the final result
print(
    f'After {investment_years} years, you will receive a total investment '
    f'revenue of {investment_revenue:,.2f} at a yearly rate of '
    f'{yearly_interest_rate}'
)