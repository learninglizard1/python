
import os

#creating class

class Pizza:

    def __init__(self, id, name, type, size):
        self.name = name
        self.id = id
        self.type = type
        self.size = size


    def message (self):
        print (f"You have ordered a {self.size} sized {self.type} {self.name} pizza. ")

os.system ('cls')

print (
    """
Please choose a pizza from the following options:
1. Meat lovers
2. Margherita
3. Italian
4. Veggie lovers
5. Classic veggie
"""
)
while True:

    option1 = input("Please choose a pizza from the given option.").strip()

    if option1 in ["1", "2", "3", "4", "5"]:
        break  # input is valid, stop asking
    else:
        print("Invalid choice, please enter a number between 1 and 5.")

if option1 == "1":
    pizza_name = "Meat lovers"

elif option1 == "2":
    pizza_name = "Margherita"

elif option1 == "3":
    pizza_name = "Italian"

elif option1 == "4":
    pizza_name = "Veggie lovers"

elif option1 == "5":
    pizza_name = "Classic veggie"
    

os.system ('cls')

print (
    """
What type of pizza would you like?
1. Standard
2. Vegeterian
3. Gluten-free
"""
)
while True:

    option2 = input("Select a type of pizza from the given option.").strip()
    
    if option2 in ["1", "2", "3"]:
        break
    else:
        print ("Invalid choice, please enter a number between 1 and 3.")

if option2 == "1":
    pizza_type  = "Standard"

elif option2 == "2":
    pizza_type  = "Vegeterian"

elif option2 == "3":
    pizza_type  = "Gluten-free"

    

os.system ('cls')

print (
    """
Please select a size:
1. Small 
2. Medium
3. Large
"""
)

while True:

    option3 = input("Select a type of pizza from the given option.").strip()
    
    if option3 in ["1", "2", "3"]:
        break
    else:
        print ("Invalid choice, please enter a number between 1 and 3.")

if option3 == "1":
    pizza_size = "Small"

elif option3 == "2":
    pizza_size = "Medium"    

elif option3 == "3":
    pizza_size = "Large"

else:
    print ("Invalid")



order = Pizza (option1, pizza_name, pizza_type, pizza_size)

order.message()