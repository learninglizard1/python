#learning to create my own abstract
print("    /////////////////////////////", "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("   ////                     ////",  "\\\\\\\\                    \\\\\\\\",sep = "---")
print("  ////      "  , "Welcome"  ,   "      ////" , "    \\\\\\\\      ", "Everyone!" , "   \\\\\\\\")
print(" ////                     ////",  "\\\\\\\\                    \\\\\\\\", sep = "-------")
print("/////////////////////////////" ,  "        \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")


#indexing
name = "Holiday"

print (name [2])
print (name[-1])
print (name[1:])
print (name[0:5])
print (name[1:5])
print (name[0:7])

#indexing    
test = "HelloWorld"

print (test[0])
print (test [0:2])
print (test [0:3])
print (test [0:4])
print (test [0:5])
print (test [0:6])
print (test [0:7])
print (test [0:8])
print (test [0:9])
print (test [:])
print (test [0:-1])
print (test [0:-2])
print (test [0:-3])
print (test [0:-4])
print (test [0:-5])
print (test [0:-6])
print (test [0:-7])
print (test [0:-8])
print (test [-10])



# Concatenation example

first_name = "John"
last_name = "Smith"
full_name = first_name + last_name
print(full_name)
# output = JohnSmith

full_name = first_name + " " + last_name
print(full_name)
# output = John Smith
    
new_name = "Prof." + " " + full_name
print(new_name)
# output = Prof. John Smith

original_match = "AUSTRALIA VS NEW ZEALAND"
part1 = original_match[0:9]                 # Extract AUSTRALIA
part2 = original_match[9:13]                # Extract VS
part3 = original_match[13:]                 # Extract NEW ZEALAND
new_match = part3 + part2 + part1           # Perform concatenation
print(original_match)
print(new_match)

    
# Useful string functions
text = "Hello world!"

# Upper text
print(text.upper())
# output = HELLO WORLD!

# Lower text
print(text.lower())
# output = hello world!

# Centre the text with whitespace
print(text.center(30))
# output =          Hello world!    

#  Centre the text and fill space with a given character
print(text.center(30,'-'))
# output = ---------Hello world!---------

# Capitalise the first character
name = "john"
print(name.capitalize())
# output = John

# Stripe the string of whitespace at the start and end
strip_example = "    Hello world!     "
print(strip_example.strip())
# output = Hello world!


#learning how to make a table
name1 = "Alice"
age1 = 25
score1 = 89.5

name2 = "Bob"
age2 = 30
score2 = 91.0


print ("Name    |  Age  |   Score  ")

print (f"{name1:<8}| {age1:>6}| {score1:>7.2f}")
print (f"{name2:<8}| {age2:>6}| {score2:>7.2f}")




#adding comma and 2 decimals
salary = 120000

print (f"Your annual salary is: ${salary:,.2f}")

#I have used a formatted string below to add a comma in between the salary by doing {salary:,} ',' helps to add commas where needed. 





#Getting texts out of dictionary by just using f-string **

    # {person['name']} grabs "name" and prints 'Charlie' 
    # {person['age']} grabs "age" and prints '28'
    # {person["hobby"]} grabs "hobby" and prints 'cycling'

person = {
    "name": "Charlie",
    "age" : 28,
    "hobby" : "cycling"
}

print(f"Name: {person['name']} | Age: {person['age']} | Hobby: {person['hobby']}")

    
#Code below is similar to the one above but it grabs nested variables inside dictionary**

# By just doing {book['author']['first_name']} it prints "F. Scott" |  we can repeat the same process with other variables.

#so to add an extra "" you can eliminate error by adding backslash '\' eg:  \"...\" 


book = {
    "title": "The Great Gatsby",
    "author": {
        "first_name": "F. Scott",
        "last_name": "Fitzgerald"
    },
    "year": 1925
}


print(f"\"{book['title'].upper()}\" by {book['author']['first_name']} {book['author']['last_name']} ({book['year']})")

#OUTPUT : "THE GREAT GATSBY" by F. Scott Fitzgerald (1925)


#String find function example

text = "She sells sea shells by the sea shore"

new_text = text.upper().replace ("S","$")
print (new_text)


#replacing words in a sentence using .replace()
sentence = "The quick brown fox jumps over the lazy dog"

sentence = sentence.replace("quick","speedy")
sentence = sentence.replace("fox","kiwi")
sentence = sentence.replace("jumps","hops")
sentence = sentence.replace("lazy","sleepy")
sentence = sentence.replace("dog","tuatara")

print (sentence)

#creating table and decimal    
product = "Notebook"
price = 4.5

print (f"Product   | Price ")
print(f"{product:<9} | ${price:.2f}")


#using """ ....... """
student = {
"name": "Eva",
"grade": 88.75,
"passed": True
}

print("Student Report:")
print(f"Name: {student['name']}")
print(f"Grade: {student['grade']}")

if student["passed"]:
    print("""
Status: Passed

Congratulations, Eva! You have successfully passed the course.
Your dedication and hard work are reflected in your excellent grade.
Keep it up!
""")
else:
    print("""
Status: Failed

Unfortunately, you did not pass this time.
Take some time to review the material and don't hesitate to ask for help.
You can do it!
""")

# Comparison operator examples

a = 10
b = 20
c = 5

result = a > c
print(result)
# output = True

result = a != 10
print(result)
# output = False
result = c + a > b
print(result)
# output = False

result = 10 / c + 20 == b + a - 8
print(result)
# output = True

result = 2 < 7 < 10
print(result)
# output = True

result = 7 <= 8 > 6
print(result)
# output = True

result = a != (b + 2) / 2 < 10.5
print(result)
# output = False


#We will go trout fishing if all conditions are met,
#1) Weather --> Sunny (S) or cloudy (C) but not rainy (R). Use one of the abbreviations
#2) Age is 20 years or more
#3) Has a trout fishing license

#Define three variables. Explore different options
weather = "C" 
age = 56
has_trout_license = True

can_fish = (weather == "R" or weather == "C") and (age >= 20) and has_trout_license
print(can_fish)
# output = False

#importing math     
import math

#circle of area calculation
radius = 2
area_circle = math.pi * radius ** 2
area_circle_rounded = round(area_circle,3)



#squarea area calculation
side = 6
area_square = side * side
area_square_rounded = round(area_square,3)

#comparison
bigger = area_circle_rounded > area_square_rounded
smaller = area_circle_rounded < area_square_rounded
same = area_circle_rounded == area_square_rounded

print (f"Circle area {area_circle_rounded} is bigger than square area {area_square_rounded}: {bigger}")
print (f"Circle area {area_circle_rounded} is smaller than square area {area_square_rounded}: {smaller}")
print (f"Circle area {area_circle_rounded} equals square area {area_square_rounded}: {same}")


#comparison of area of a circle and area of a square

area_of_circle = 12.566
area_of_square = 36

bigger = area_of_circle > area_of_square
smaller = area_of_circle < area_of_square
equal = area_of_circle == area_of_square

print (f"Circle area {area_of_circle} is bigger than square area {area_of_square}: {bigger}")

print (f"Circle aera {area_of_circle} is smaller than squaer area {area_of_square}: {smaller}")

print (f"Circle area {area_of_circle} equals to square area {area_of_square}: {equal}")


# Introduction to if statements

# Some variables just for example
shop_open = False
player_strength = 10
rock_weight = 7
student_mark = 85
minimum_mark = 50
player_gold = 6
item_cost = 7
  
# A small shop in our RPG where players can buy items
if(shop_open == False):
    print("The shop is closed... We'll have to come back later.")

# Trying to lift a rock
if(player_strength > rock_weight):
    print("The rock rolls out of the way. The path is now clear!")

# Did the student pass the test?
if(student_mark > minimum_mark):
    print("Congratulations! You passed!")

# Can we afford an item in the store?
if(player_gold >= item_cost):
    print("You have enough to buy the item.")
else:
    print("Hmm this is a tough decision...")

     
# Introduction to if statements

    shop_open = True
    is_energised = False
    
    print("You walk up to the shop and check the door.")
    if(shop_open == True):
        print("The shopkeeper welcomes you.")
        print("The shopkeeper asks if you would like a sample potion.")
        has_accepted_offer = input("Do you want to accept the potion? (y/n)")
        if(has_accepted_offer == "y"):
            print("The shopkeeper hands you the potion.")
            has_drunk_potion = input("Would you like to drink the potion? (y/n)")
            if(has_drunk_potion == "y"):
                print("You drink the potion in one gulp. You feel energized!")
                is_energised = True
        print("The shopkeeper gestures for you to browse the shop.")
        print("You leave the shop.")
    if(is_energised):
        print("Feeling all this extra energy you decide to run to the next location!")
    
    print("The sun starts to set. It's time to find an inn for the night.")



# If elif else conditions

    number = int(input("Enter a number:"))
    
    if(number > 0):
        print("Number is positive")
    elif(number < 0):
        print("Number is negative")
    else:
        print("Number is neither positive nor negative")


#Converting to integer    
    user = input ("Enter a number:")
    change = int(user)
    
    if (change > 0):
        print ("The number is higher than zero")
    else:
        print("The number is equal to / lower then zero")


#check if the number is odd or even
    number = int(input("Enter a number:"))

    if number % 2 == 0:
        print (f"{number} is an even number")
    else:
        print (f"{number} is an odd number")



#if elif and else statement practice        
    age = int(input("Enter your age:"))
    
    if age <= 0 :
        print ("Error! there is no such age ")
    elif age <= 12:
        print ("Child")
    elif age <= 19:
        print("Teenager")
    elif age <=64:
        print("Adult")
    else:
        print("Senior")

#if elif and else statement practice               
    num1 = int(input("Enter your first number:"))
    num2 = int(input("Enter your second number:"))
    
    if num1 > num2:
        print (f"{num1} is greater than {num2}.")
    elif num2 > num1:
        print (f"{num2} is greater than {num1}.")
    else:
        print (f"{num1} and {num2} are equal")


      
# Error checking - No value entered
    number = input("Enter number:")
    
    if (number.strip() == ""):
        print("You have not entered a value")

#stripping (-) from negative number  

    number = input("Enter a number:")
    
    if number.lstrip('-').isdigit():
        integer = int(number)
        if (integer > 0):
            print ("Number is positive.")
        elif (integer < 0):
            print ("Number is negative.")
        else:
            print ("Number is neither positive or negative")
    else:
        print("Please enter a valid digit")


 #error checking and nested if else statements       
    number = input("Enter a number:")
    
    if number == "":
        print ("INVALID!")
    else:
        strip = number.strip()
        change = int(number)
        if(change > 0):
            print("Number is positive")
        elif(change < 0):
            print("Number is negative")
        else:
            print("Number is neither positive nor negative")



# Error checking - Valid data type

    error_found = False         # Assume no error until we find one
    number = input("Enter number:")
    
    number = number.strip()     # Strip the string of whitespace before/after
    
    if(number == ""):
        print("Error: No value entered")
        error_found = True
    
    if(number.isdigit() == False):
        print("Error: Contains invalid characters")
        error_found = True
    
    # Only continue if no error was found
    if(error_found == False):
        number = int(number)
    
        # Now we can use our number in equations or however you want
        result = ((number * 2) / 6)
        print("Result of our fancy equation: ", str(result))
    else:
        # Cancel the current action
        # Later we'll learn how to return to previous code and try again
        pass


        
#Error checking and character test

    code_error = False
    name = input("Enter your name:")
    
    if name == " ":
        print("No spaces allowed")
        code_error = True
    
    if (name.isalpha() == False):
        print ("Only alphabets! and no spaces are allowed.")
        code_error = True
    
    
    if (code_error == False):
        name = str(name)
    
        if (len(name) < 3 and len(name) > 20):
            print (f"Welcome {name}")
        else:
            print("Please enter characters between 3 to 20")
    else:
        print("ERRROORRRRR")       


#factorial
    number = int(input("Enter a number:"))
    factorial = 1
      
    for i in range (1, number + 1):
          factorial *=i
    print (factorial)


      
# While example

    total = 0
    
    number = int(input("Enter first number:"))
    
    # If the user enters 0 or a negative number, cancel the loop
    while(number > 0):
        total = total + number
    
        number = int(input("Enter new number: "))

      # Display the final total
    print("Total =", total)


#while loop       
    total = 0
    
    while True:
        number = int(input("enter a number(0 to stop):"))
    
        if number == 0:
            break
        total += number
    
    print (f"Total = {total}")


#learning 'break' inside a while loop
word = "python"
      
while True:
    something = str(input("whats the best programming langugae?"))

    if something != word:
        print ("Wrong!")
    else:
        break
print ("correct!")


#error checking and while loop
while True:
    number = input("Enter a number higher than 10:")

    number = number.strip()

    if number == "":
        print ("Invalid input, Please enter a number")
        continue    
        
    if not number.isdigit():
        print ("Only digits are allowed.")
        continue

    number = int(number)
    
    if (number <= 10):
        print("Too small, try again!")
        continue
    
    break
print ("Thank you")




#(try and except) error checking

while True:
    number = input ("Enter a number:")
    number = number.strip()

    if number == "":
        print ("Invalid no numbers entered")
        continue

    try:
        yawa = float(number)
    except ValueError:
        print ("Only digits are allowed.")
        continue

    if yawa <= 10:
        print ("The number is too low")
        continue

    break
print ("Thank you")

# for loop
user_input = input("Type something")
    
for i in user_input:
    i *= 4
    print (i)

           

# List exercise - Building some words 

consonents = ["h", "k", "m", "n", "ng", "p", "r", "t", "w", "wh"] 
vowels = ["a", "e", "i", "o", "u"] 

print (consonents [1], vowels [0], vowels [2], " ", consonents[2], vowels [-2], vowels [0], consonents [3], vowels [0])

print (vowels[0], consonents [-4], vowels[-2], consonents[0], vowels[-5])

print (consonents [1], vowels [2], vowels[0], " ", vowels[-2], consonents[-4], vowels[0])



# creating loops

names = [ "John", "Arana", "Susan", "Marsha", "Ahmad", "Bing"]

ages = [21, 45, 19, 33, 57, 42]

scores = [78.8, 90.3, 89, 49, 23.7, 88.9]


for all in range(len(names)):
    print (names[all], " aged ", ages[all], " scored ", scores[all], " in BIT502.")


    
#creating loops same as above but with variable

names = [ "John", "Arana", "Susan", "Marsha", "Ahmad", "Bing"]

ages = [21, 45, 19, 33, 57, 42]

scores = [78.8, 90.3, 89, 49, 23.7, 88.9]

total = range(len(names))

for all in total:
    print (names[all], " aged ", ages[all], " scored ", scores[all], " in BIT502.")


#using for loop
names = ["John", "Arana", "Suzan", "Marsha", "Ahmad", "Bing"]

loop = range(len(names))

result = ""

for i in loop:
    if 'a' in names[i].lower():
        result += names[i]

print (result)


#searching letter in a list

names = [ "John", "Arana", "Suzan", "Marsha", "Ahmad", "Bing"]
letter = input("Search:")
result = ""

for name in names:
    lower_name = name.lower()
    if letter in lower_name:
        index = lower_name.index(letter)
        result += str(index + 1)
    else:
        result += "0"

print (result)


#sorting and reversing
numbers = [ 32, 2, 12, 57, 34, -1, 53, 22, 10, 2, 12, 14]

numbers.sort()

print (numbers[-1])

numbers.reverse()

print (numbers)

while True:
    check = int(input("Enter a number:"))
    if check in numbers:
        while check in numbers:
            numbers.remove(check)
        print("Updated number list:", numbers)
        break
    else:
        print("The number is not in the list.")


# append to the list 
names = []

while True:
    name = str(input("Enter a name:").strip())

    if name == "*":
        break
    
    if name == "":
        print ("Error! enter a name")
    else:
        names.append(name)    
        print ("Enter name:",name)


print (names)


# learning to create a menu and using pass to enter options later

import os
clear = lambda: os.system('cls')


while True:
    print ("Welcome to my shop, what would you like to do?")

    print("1. Buy item")
    print("2. Sell item")
    print("3. Talk")
    print("4. Leave shop")

    option = input("Enter your option:")

    if (option == "1"):
        pass
    elif (option == "2"):
        pass
    elif (option == "3"):
        pass
    elif (option == "4"):
        print("THank you for visiting")
        break
    else:
        print ("Invalid option. Please try again.")
        continue


        
# Menu example

# Import the os library, this gives us access to the ability to clear the screen
import os

player_gold = 200

while(True):

    # Clear the terminal screen and display the menu fresh
    os.system("cls")

    # Display menu explanation introduction
    print("Welcome to my shop! Got a selection of good things on sale!")

    # Display the menu options
    print("1. Buy item")
    print("2. Sell item")
    print("3. Talk")
    print("4. Leave shop")

    # Prompt for input
    option = input("Enter your option:")

    # Branch code based on option
    if(option == "1"):
        while(True):

            # Clear the terminal screen and display the menu fresh
            os.system("cls")

            # Display menu info
            print("What're ya buyin, stranger?")

            # Display menu items
            print("1. Potion")
            print("2. Shield")
            if(player_gold > 100):
                print("3. Secret item")
            print("4. Return to previous menu")

            # Prompt for input
            choice = input("Enter your option:")

            # Branch code based on option
            if(choice == "1"):
                print("You buy a potion")
                
                # Wait until the user presses enter before continuing
                input("Press enter to continue...")
                continue
            elif(choice == "2"):
                print("You buy a shield")
                
                # Wait until the user presses enter before continuing
                input("Press enter to continue...")
                continue
            elif(choice == "3" and player_gold > 100):
                print("You buy the secret item!")
                
                # Wait until the user presses enter before continuing
                input("Press enter to continue...")
                continue
            elif(choice == "4"):
                print("Returning to previous menu.")
                
                # Wait until the user presses enter before continuing
                input("Press enter to continue...")
                break
            else:
                print("Invalid option. Please try again.")
                
                # Wait until the user presses enter before continuing
                input("Press enter to continue...")
                continue

    elif(option == "2"):
        print("Sorry stranger, can't buy items off you right now")
        
        # Wait until the user presses enter before continuing
        input("Press enter to continue...")
        continue
    elif(option == "3"):
        print("Nice weather we're having right now")
        
        # Wait until the user presses enter before continuing
        input("Press enter to continue...")
        continue
    elif(option == "4"):
        print("Come back anytime.")

        # Wait until the user presses enter before continuing
        input("Press enter to continue...")
        break
    else:
        print("Invalid option. Please try again.")
        
        # Wait until the user presses enter before continuing
        input("Press enter to continue...")
        continue


        
# Defining functions


# Prints the hello world message to the user
def my_first_function():
    print("Hello world!")


# Welcomes the user with a message
# name = the name of the person we are welcoming
def my_second_function(name):
    print(f"Kia ora, {name}!")


# Caclculates the sum of two numbers
# number1 = the first number
# number2 = the second number
def addition(number1, number2):
    result = number1 + number2
    return result

addition ( 9 , 10)


#calling function 3x
def hello_display():
    print("How are you?")

#Your initial code
name = input("Enter your name: ")
print("Hi " + name)
hello_display()
hello_display()
hello_display()
print("Bye for now!")




# Function example - Calculate area of circle
import math

# Define our function
def area_circle_calculator(r):
    area = math.pi * r ** 2
    print(f"Area of a circle with radius of {r} is {area}")

# Prompt for input (error checking has been skipped to keep example small)
radius = int(input( "Enter the radius of a circle: "))

# Call our function with radius as the argument
area_circle_calculator(radius)



# Function example - Multiple parameters

def display_personal_info(age, last_name, first_name):
    print(first_name + " " + last_name + " With age: " + str(age))

# Our code execution will begin here

# Note: Error checking skipped for example
number = int(input("Enter Age: "))
f_name = input("Enter first name: ")
l_name = input("Enter last name: ")

# Note: The variables do not need to match the names of the parameters
display_personal_info(number,l_name,f_name)




# Function example - Using static arguments
display_personal_info(32, "Valentine", "Jill")



# Making use of functions 

def request_input(message): 
    result = input(message) 
    # NOTE: Error checking and validation skipped for example 
    # It would be great to practice your error checking here 
    return result 

# J. Smith 
def first_initial_with_lastname(first, last): 
    return first[0:1] + ". " + last 


# Smith, John 
def lastname_firstname(first, last): 
    return last + ", " + first 


# Smith, J 
def lastname_first_initial(first, last): 
    return last + ", " + first[0:1] 


# J. S 
def initials_only(first, last): 
    return first[0:1] + ". " + last[0:1] 


first = request_input("Enter first name:") 
last = request_input("Enter last name:") 


# J. Smith 
print(first_initial_with_lastname(first, last)) 


# Smith, John 
print(lastname_firstname(first, last)) 


# Smith, J 
print(lastname_first_initial(first, last)) 


# J. S 
print(initials_only(first, last)) 



#assignning variable to call function
def names( title, lname , fname):
    return (f"Your full name is {title} {fname} {lname}.")

whole = names( "Mr.", "Doe" , "John")

print (whole)


#calculation using an operator
def calculator ( a, b, operator):
    
    if operator == "+":
        print (f"Addition of {a} and {b} is: {a + b}")
    elif operator == "-":
        print (f"The subtration of {a} and {b} is: { a- b }")
    elif operator == "*":
        print (f"The multiplication of {a} and {b} is: {a * b}")
    elif operator == "/":
        if b == 0:
            print("You cant divide by 0")
        else:
         print (f"The division of {a} and {b} is: {a / b:.2f}")        
    else:
        print ("Invalid!")

calculator(a = 29, b = 7, operator = "/")


def old (full_name, age):
    if age < 18:
        message = (f"{full_name} you are not elibible to attend.")

    else:
        vaccine_pass = input("Do you have a vaccine pass? (y/n)")

        if age >= 50 and vaccine_pass == "y":
            message = f"{full_name} go to Hall A."
        elif age >= 50 and vaccine_pass == "n":
            message = f"{full_name}  go to Hall B."
        else:
            message = f"{full_name} go to Hall C."

    return full_name, message, age

first_name = input("Enter your first name:")
last_name = input("Enter your last name: ")
age = int(input("Enter your age:"))

full_name = (f"{first_name} {last_name}")
ame, reply, agegap = old (full_name , age)


print (reply)

# Function example - functions calling other functions

def function1():
    print("I am in function1")
    function2()
    print("I am back to function1")

def function2():
    print("I am in function2")
    function3()
    print("I am back to function2")
    function4()
    print("I am back to function2")

def function3():
    print("I am in function3")

def function4():
    print("I am in function4")


#Main code
print("I am in the main code")
function1()
print("I am back to the main code")
function4()
print("I am back to the main code")
def function1(): 
    print("I am in function1") 
    function2() 
    print("I am back to function1") 

def function2(): 
    print("I am in function2") 
    function3() 
    print("I am back to function2") 
    function4() 
    print("I am back to function2") 

def function3(): 
    print("I am in function3") 

#Change this code for this whole thing to become an infinite nested function 
def function4(): 
    print("I am in function4") 
    # Hint: Place a call to function2() here 
    print("I am in function4 again") 

#Main code 
print("I am in the main code") 
function1() 
print("I am back to the main code") 
function4() # this triggers the infinite nested function behaviour 
print("I am back to the main code")
# Code modification


def function1():
    # This variable will be local
    a = 6
    print("Function 1:", a)


def function2():
    # This function will request to use the variable from the global scope
    global a
    print("Function 2:", a)


a = 9
function1()
function2()
print("Main code:", a)
# Code modification


def function1():
    # This variable will be local
    a = 6
    print("Function 1:", a)


def function2():
    # This function will request to use the variable from the global scope
    global a
    a = 200
    print("Function 2:", a)


a = 9
function1()
function2()
print("Main code:", a)


# Error checking - Valid integer in a function

def prompt_for_integer(message: str = "Enter number:"):
    # Loop until we get the correct value
    while(True):
        error_found = False         # Assume no error until we find one
        number = input(message)     # Prompt the user for input

        number = number.strip()     # Strip the string of whitespace before/after

        if(number == ""):           # Blank input found
            print("Error: No value entered")
            error_found = True

        elif(number.isdigit() == False):  # Contains invalid characters
            print("Error: Contains invalid characters")
            error_found = True
        
        # Error has been found, restart the loop
        if(error_found == True):
            continue

        # No error was found, return the result
        return int(number)
    
prompt_for_integer()
# Code without error checking

num = float(input("Enter number:"))

result = 100 / num

print(result)
# Try...except example

try:
    num = float(input("Enter number:"))

    result = 100 / num

    print(result)
except:
    print("ERROR: An error occurred")
# Try...except example

# You can place code above or below the try except block
print("Welcome!")

# Our try except block
try:
    num = float(input("Enter number:"))
except:
    print("ERROR: An error occurred")

# Outside of the try except block, back to our normal block

result = 100 / num

print(result)
try:
    
    one = float(input('Number one:'))
    two = float(input('Number two:'))

    change = (two - one) * 100 / one

    if change > 0:
        print(f'Number increased {abs(change)}%')
    else:
        print(f'Number decreased {abs(change)}%')

except:     
    print('Enter two numbers')
finally:
    print('Finishing up.')
    
try:
    print ("Enter two numbers: ")

    try:
        one = float(input('Number one:'))
    except:
        print ("ERROR: An error occured.")
    try:
        two = float(input('Number two:'))
    except:
        print ("ERROR: An error occured.")
    

    change = (two - one) * 100 / one

    if change > 0:
        print(f'Number increased {abs(change)}%')
    else:
        print(f'Number decreased {abs(change)}%')

except ZeroDivisionError as error:
     print(error)

finally:

    print('Finishing up.')






#Instantiating objects of classes

class Shape:
    pass

#instantiate our variables
square = Shape()
triangle = Shape()
pentagon = Shape()


#Set the member variables
square.name = "Square"
triangle.name = "Triangle"
pentagon.name  = "Pentagon"
square.sides = 4
triangle.sides = 3
pentagon.sides = 5

#print the method
print (f"{square.name} has {square.sides} sides.")
print (f"{triangle.name} has {triangle.sides} sides.")
print (f"{pentagon.name} has {pentagon.sides} sides.")
