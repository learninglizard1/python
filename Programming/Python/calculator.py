# Calculator

import os
import sys
import math

def addition (numbers):
    return (numbers)

def subtract (num1 , num2):
    return (num1 - num2)

def multiply (num1 , num2):
    return (num1 * num2)

def divide (num1 , num2):
    return (num1 / num2)

def exponent (num1):
    return num1 ** num1

def pi(r):
    return math.pi * r ** 2

def square(num1):
    return math.sqrt(num1)

def modulus(num1):
    return num1 % 2
    


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
        print ("6. Area of a circle.")
        print ("7. Square root.")
        print ("8. Find odd or even")
        print ("9. Exit")

        option = input("\nPlease select an option.").strip()
    
        os.system ('cls')
        
        if option == "":
            print ("Please enter a number between 1 to 9 to select from the given menu.")
            input ("Press enter to continue...")
            continue

        elif not option.isdigit():
            print ("Error! only digits are allowed.")       
            input("Press enter to continue...")
            continue
        
        elif option == "1":
            store = []
            while True:
                try:
                    num1 = (input ("Enter a number to add: "))
                    
                    num1 = float(num1)

                    store.append(num1)

                    if num1 == 0:
                        print(f"Total sum = {sum(store):.2f}.")
                        input("Press enter to continue..")
                        break
                    else:
                        print("enter another number to add or 0 to print the sum:")
                except ValueError:
                    print("Only digits allowed.")
                    continue

        elif option == "2":
            while True:
                try:
                    num1 = float(input ("Enter your first number: "))
                    num2 = float(input("Enter your second number:"))
                    print(f"{num1} - {num2} = {subtract(num1, num2)}.")
                    input("Press enter to continue..")
                except ValueError:
                    print("Only digits allowed.")
                    continue

        elif option == "3":
            while True:
                try:
                    num1 = float(input ("Enter your first number: "))
                    num2 = float(input("Enter your second number:"))
                    print(f"{num1} * {num2} = {multiply(num1, num2)}.")
                    input("Press enter to continue..")
                except ValueError:
                    print("Only digits allowed.")
                    continue

        elif option == "4":
            while True:
                try:
                    num1 = float(input ("Enter your first number: "))
                    num2 = float(input("Enter your second number:"))
                    
                    if (num2 == 0):
                        print ("You cant divide a number by 0. Returning back to the menu")
                        input("Press enter to continue...")
                    else:
                        print(f"{num1} / {num2} = {divide(num1, num2):.2f}.")
                    input("Press enter to continue..")      
                except ValueError:
                    print("Only digits allowed.")
                    continue

        elif option == "5":
            while True:
                try:
                    num1 = float(input ("Enter a number:"))
                    print(f"{num1} ^ {num1} = {exponent(num1)}")
                    input("Press enter to continue..")
                except ValueError:
                    print("Only digits allowed.")
                    continue

        elif option == "6":
            while True:
                try:
                    r = float(input ("Enter a radius::"))
                    print(f"The area of a circle is {pi(r):.2f}")
                    input("Press enter to continue..")
                except ValueError:
                    print("Only digits allowed.")
                    continue

        elif option == "7":
            while True:
                try:
                    num1 = float(input ("Enter a number::"))
                    print(f"The square root of {num1} is {square(num1)}")
                    input("Press enter to continue..")
                except ValueError:
                    print("Only digits allowed.")
                    continue

        elif option == "8":
            while True:
                try:
                    num1 = int(input ("Enter a number to find if its odd or even: "))
                    if num1 %2 == 0:
                        print (f"{num1} is an Even number.")
                    else:
                        print (f"{num1} is an Odd number.")
                    input("Press Enter to continue...")
                except ValueError:
                    print("Only digits allowed.")
                    continue

        elif option == "9":
            sys.exit()

        else:
            print ("Invalid. Enter a number between 1 to 9.")
            input("Press enter to continue..")




calculator()
