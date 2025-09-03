# Listbox example

# Imports
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox

# Set up window
root = tk.Tk()
root.geometry('200x250')
root.resizable(False, False)
root.title("Listbox demo")

# Define our function for the listbox click event
# You can name this anything that makes sense for you
# We need to have the "event" parameter, the listbox expects this
def listbox1_clicked(event):
    # Obtain the listbox item that was clicked
    # This will give you a result like (1,) if you clicked the second item or (0,) if you clicked the first
    item_clicked = listbox.curselection()       # Cursor selection
    # We want to get the actual value of the item rather than the index
    item = listbox.get(item_clicked)
    # Now the item variable will hold the text of what was clicked
    # Show infomation
    msgbox.showinfo("Clicked", "You clicked " + item)

# Create our listbox widget
# NOTE: ttk does not have the listbox so we use standard tk
listbox = tk.Listbox(root, height = 10)

# Position widgets
listbox.grid(row = 0, column = 0, padx=10, pady=10)

# Insert some values into the listbox
# We use tk.END to add it to the end of the list, you could specify a number if you prefer
listbox.insert(tk.END, "Apple")
listbox.insert(tk.END, "Banana")
listbox.insert(tk.END, "Coconut")
listbox.insert(tk.END, "Dragon Fruit")
listbox.insert(tk.END, "Elderberry")
listbox.insert(tk.END, "Fig")
listbox.insert(tk.END, "Guava")
listbox.insert(tk.END, "Hackberry")
listbox.insert(tk.END, "Imbe")
listbox.insert(tk.END, "Jackfruit")
listbox.insert(tk.END, "Kiwifruit")

# Click functionality
# To have something happen when the user clicks an item in the list we need to bind an event
listbox.bind("<<ListboxSelect>>", listbox1_clicked)

root.mainloop()
