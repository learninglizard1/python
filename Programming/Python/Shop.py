#importing tkinter

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Shop")

group1_labels = {
    1: "Health",
    2: "Stamina",
    3: "Magic"
}
group1_prices = {
    1: 10,  # Health
    2: 10,  # Stamina
    3: 12   # Magic
}

group2_labels = {
    4: "Small",
    5: "Medium",
    6: "Large"
}
group2_prices = {
    4: 0,   # Small (no extra cost)
    5: 5,   # Medium
    6: 10   # Large
}

strong_bottle_price = 8

def button_clicked():
    total = 0

    selected_item = group1.get()
    selected_size = group2.get()

    total += group1_prices.get(selected_item, 1)
    total += group2_prices.get(selected_size, 1)

    item_name = group1_labels.get(selected_item , "Unknown")
    size_name = group2_labels.get(selected_size, "Unknown")
    price1 = group1_prices.get(selected_item, 0)
    price2 = group2_prices.get(selected_size, 0)
    total = price1 + price2
    
    if stronger.get():
        total += strong_bottle_price
        message1 = (
            f"You have purchased: {item_name} ({price1})\n"
            f"Size: {size_name} ({price2})\n"
            f"Optional price: {strong_bottle_price}\n"
            f"Total cost : {total}"
        )
        messagebox.showinfo ("Shop", message1)
    
    else:
        message2 = (
            f"You have purchased: {item_name} ({price1})\n"
            f"Size: {size_name} ({price2})\n"
            f"Total cost : {total}"
        )
        messagebox.showinfo ("Shop", message2)



group1 = tk.IntVar(value = 1)
group2 = tk.IntVar(value = 4)
stronger = tk.IntVar()

#first group of radio buttons
tk.Label (root, text="Select Item type:").pack()
health = tk.Radiobutton(root, text= f"Health (10 gold)", variable= group1, value= 1)
health.pack()
stamina = tk.Radiobutton (root, text= f"Stamina (10 gold)", variable = group1, value= 2)
stamina.pack()
magic = tk.Radiobutton(root, text= f"Magic (12 gold)", variable= group1, value= 3)
magic.pack()

#label in the middle to separate radio buttons
label = tk.Label (root, text="~~~~~~~~~~~~~~~~~~~~~").pack()


#second group of radio buttons
tk.Label (root, text="Select Size:").pack
small = tk.Radiobutton (root, text= "Small", variable= group2, value= 4)
small.pack()
medium = tk.Radiobutton (root, text= "Medium", variable= group2, value= 5)
medium.pack()
large = tk.Radiobutton (root, text= "Large", variable= group2, value= 6)
large.pack()

checkbutton = tk.Checkbutton (root, text= "Stronger bottle", variable= stronger)
checkbutton.pack()

button = tk.Button (root, text = "Submit", command= button_clicked)
button.pack()


root.mainloop()



#using global * to import tkinter so we dont need to call in every variable or function.
from tkinter import *
from tkinter import messagebox


def ButtonEvent():
    messagebox.showinfo ("Alert notice", "This is a message box")

def ExitApp():
    exit()


root = Tk()
root.title("Events demo")

text_label = Label(root, text="This is text").grid (row= 0, column= 0)

button_go = Button(root, text="Go", width= 15, command = ButtonEvent)
button_go.grid (row=1 , column= 0)

button_next = Button(root, text= "Next", width = 15, command= ButtonEvent)
button_next.grid (row=1, column=1)

button_before = Button(root, text= "Before", width= 15, command= ButtonEvent)
button_before.grid (row=1, column=2)

button_exit = Button(root, text= "Exit", width= 15, command= ExitApp)
button_exit.grid (row=1, column=3)


root.mainloop()
