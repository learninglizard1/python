# Calculator

import os

def addition (num1, num2):
    return (num1 + num2)

def subtract (num1 , num2):
    return (num1 - num2)

def multiply (num1 , num2):
    return (num1 * num2)

def divide (num1 , num2):
    return (num1 / num2)

def exponent (num1):
    return num1 ** num1


def calculator():
    while True:
        os.system ('cls')
        #printing welcome message
        print ("Welcome to the calculator".center(50, "-"))
        print ("\n1. Addition.")
        print ("2. Subtraction.")
        print ("3. Multiplication")
        print ("4. Division.")
        print ("5. Exponential.")

        option = input("\nPlease select an option.").strip()
    
        os.system ('cls')

        if option == "":
            print ("Please enter a number between 1 to 5 to select from the given menu.")
            input ("Press enter to continue...")
            continue

        elif not option.isdigit():
            print ("Error! only digits are allowed.")       
            input("Press enter to continue...")
            continue

        elif option == "1":
            num1 = int(input ("Enter your first number: "))
            num2 = int(input("Enter your second number:"))
            print(f"{num1} + {num2} = {addition(num1, num2)}.")
            input("Press enter to continue..")

        elif option == "2":
            num1 = int(input ("Enter your first number: "))
            num2 = int(input("Enter your second number:"))
            print(f"{num1} - {num2} = {subtract(num1, num2)}.")
            input("Press enter to continue..")

        elif option == "3":
            num1 = int(input ("Enter your first number: "))
            num2 = int(input("Enter your second number:"))
            print(f"{num1} * {num2} = {multiply(num1, num2)}.")
            input("Press enter to continue..")

        elif option == "4":
            num1 = int(input ("Enter your first number: "))
            num2 = int(input("Enter your second number:"))
            
            if (num2 == 0):
                print ("You cant divide a number by 0. Returning back to the menu")
                input("Press enter to continue...")
            else:
                print(f"{num1} / {num2} = {divide(num1, num2):.2f}.")
            input("Press enter to continue..")      

        elif option == "5":
            num1 = int(input ("Enter a number:"))
            print(f"The exponent of num1 is {exponent(num1)}")
            input("Press enter to continue..")

        else:
            print ("Invalid. Enter a number between 1 to 5.")
            input("Press enter to continue..")




calculator()