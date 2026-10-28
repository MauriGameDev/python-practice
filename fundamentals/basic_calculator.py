# This python program is called 'Basic Calculator'
# The user will pick 2 numbers and operation
# add, subtract, multiply, and divide

#function for Menu
def displayMenu():
    print("+-------------------------------------------------------------------+")
    print("|                         Basic Calculator                          |")
    print("| Instructions: enter numbers then operation, End program when done |")
    print("|                     press Y/N to End program                      |")
    print("+-------------------------------------------------------------------+")
    print("  (+)Add   (-)Subtract     (*)Multiply     (/)Divide   (=)Process   ")


#display menu
displayMenu()

#variable for operations
option = 0

#variable to end program
endProg = False

#line break
print("\n")


#Loop for program
while True:
    #Get first number
    try:
        num1 = float(input("Enter first number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    #Get Operations
    try:
        option = int(input("Enter operation: (1) Add (2) Subtract (3) Multiply (4) Divide:\n"))
    except ValueError:
        print("Invalid operation")
        continue
    
    #Get Second number
    try:
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
            
    
    #process operations
    if option == 1:
        answer = num1 + num2
        print(f"Display: {num1} + {num2} = {answer}")
    
    elif option == 2:
        answer = num1 - num2
        print(f"Display: {num1} - {num2} = {answer}")
        
    elif option == 3:
        answer = num1 * num2
        print(f"Display: {num1} x {num2} = {answer}")
    
    elif option == 4:
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            answer = num1 / num2
            print(f"Display: {num1} / {num2} = {answer}")
    else:
        print("Invalid operation. Please enter 1, 2, 3, or 4.")
        
    #Ask if user wants to end program
    endProg = str(input("Do you want to End program: (Y/N): ")).upper()
    if endProg == "Y":
        break
        

print("Goodbye!")
    
    

