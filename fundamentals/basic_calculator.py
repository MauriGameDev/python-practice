# This python program is called 'Basic Calculator'
# The user will pick 2 numbers and operation
# add, subtract, multiply, and divide

#function for Menu
def displayMenu():
    print("+-------------------------------------------------------------------+")
    print("|                         Basic Calculator                          |")
    print("| Instructions: enter numbers then operation, End program when done |")
    print("|                     press Y/N to End program                        |")
    print("+-------------------------------------------------------------------+")
    print("  (+)Add   (-)Subtract     (*)Multiply     (/)Divide   (=)Process   ")


#display menu
displayMenu()

#variable for operations
option = 0

#variable to end program
endProg = False

#run while loop to get numbers
while endProg != True:
    num1 = float(input("Enter number: "))
    option = int(input("Enter operations: (1)Add   (2)Subtract     (3)Multiply     (4)Divide: "))
    num2 = float(input("Enter number: "))
    
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
        answer = num1 / num2
        print(f"Display: {num1} / {num2} = {answer}")
    
    endProg = str(input("Do you want to End program: (Y/N): ")).upper()
    if endProg == "Y":
        endProg = True
    else:
        endProg = False
        

print("Goodbye!")
    
    

