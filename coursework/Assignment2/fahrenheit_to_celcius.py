#Prompt the user for a temperature in fahrenheit 
fahrenheit = float (input('Please enter a degree in Fahrenheit: '))

#Perform converserion to Celsius
celsius = (fahrenheit -32) * 5/9

#Generate th eoutput using f-string to format the result 
print(f'{fahrenheit} degrees farenheit is {celsius:.2f} degrees celcius')