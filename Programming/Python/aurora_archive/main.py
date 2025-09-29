#### Name: Sachin Bade	
#### Student No. 5117566	
#### BIT502 Assessment 3

import tkinter as tk
from tkinter import messagebox as mb
import file_window
import membership_window
import search_window
import statistics_window
import help_window

root = tk.Tk()
root.title ("The Aurora Archive")
root.geometry ("600x400")
root.resizable (False, False)


# Functions

# Added open and save menu for future proof 
def menu_file_open ():
    file_window.open_file()

def menu_file_save():
    file_window.save_file()

def menu_members():
    membership_window.show_membership(root)

def menu_statistics():
    statistics_window.show_statistics(root)

def menu_search():
    search_window.show_search(root)

def menu_help():
    help_window.show_help(root)  # Link to help python file

def exit():
    answer = mb.askyesno("The Aurora Archive", "Would you like to exit the program?")
    if answer:
        root.destroy()

# Tkinter menu setup
menubar = tk.Menu(root)
root.config (menu = menubar)

# Menu options
file_menu = tk.Menu(menubar, tearoff= False)
member_menu = tk.Menu(menubar, tearoff= False)
statistics_menu = tk.Menu(menubar, tearoff= False)
search_menu = tk.Menu(menubar, tearoff= False)
help_menu = tk.Menu(menubar, tearoff= False)


# Add menus to the menubar
menubar.add_cascade(label = "File", menu=file_menu)
menubar.add_cascade(label = "Membership", menu= member_menu)
menubar.add_cascade(label = "Statistics", menu = statistics_menu)
menubar.add_cascade(label = "Search", menu = search_menu)
menubar.add_cascade(label = "Help", menu = help_menu)


# Menu Commands
file_menu.add_command(label = "Open", command= menu_file_open)  # Open command
file_menu.add_command(label = "Save", command= menu_file_save)  # Save command   
file_menu.add_separator()                                       # Separator in the menu
file_menu.add_command (label = "Exit", command= root.quit)      # Exit command

member_menu.add_command (label = "Membership Form", command = menu_members) # Membership

statistics_menu.add_command(label ="Statistics", command = menu_statistics) # Statistics

search_menu.add_command(label = "Search", command = menu_search) # Search

help_menu.add_command (label = "About..", command= menu_help) # Help


# Widgets
welcome = tk.Label(root, text= "Welcome to Aurora Archive", font= ("Tahoma", 28, "bold"), fg="red")
btn_membership = tk.Button(root, text= "Membership Form", command= menu_members, font= ("New Courier", 15, "bold"), relief= "solid", width= 30 , bg= "#C5CCE9")
btn_search = tk.Button(root, text= "Search", command= menu_search, font= ("New Courier", 15, "bold"), relief= "solid", width= 30, bg= "#C5CCE9")
btn_statistics = tk.Button (root, text= "Statistics", command= menu_statistics, font= ("New Courier", 15, "bold"), relief= "solid", width= 30, bg= "#C5CCE9")
btn_help = tk.Button (root, text= "Help", command= menu_help, font= ("New Courier", 15, "bold"), relief= "solid", width= 30 , bg= "#C5CCE9")
btn_exit = tk.Button (root, text= "Exit", command= exit, font= ("New Courier", 15, "bold"), relief= "solid" , width= 30, bg= "red")

# Widget positions
welcome.grid (row= 0, column= 0, columnspan = 2, padx= (50, 0))

btn_membership.grid(row= 1, column=0, padx= (90, 0), pady= 10)
btn_search.grid(row= 2, column= 0, padx= (90, 0), pady= 10)
btn_statistics.grid(row=3, column= 0, padx= (90, 0), pady= 10)
btn_help.grid(row= 4, column= 0, padx= (90, 0), pady= 10)
btn_exit.grid(row= 5, column= 0, padx= (90, 0), pady= 10)


root.mainloop()