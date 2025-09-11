
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.geometry("700x450")
root.title("Search database")
database_name = "fruit.db"
table_name = "Fruit"

####################
# Database functions
# NOTE: Trimed functions down to minimal code for examples

def execute_query(query):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()

def select_query(query):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows

# END Database functions
########################

########################
# Build search query

# The submit button will search through the options and build our query
def submit():
    query = ""

    # Read the GUI widgets and build string
    global edit_name
    global edit_colour
    global edit_taste

    # Build query here
    query = f"SELECT * FROM {table_name}"

    # If a query has been built, you could do additional validation too
    if(query):      
        rows = select_query(query)      # Run our query to get rows
        update_treeview(rows)           # Update the treeview with our rows



# END Build search query
########################


########################
# Search widgets

edit_name = tk.StringVar()
edit_colour = tk.StringVar()
edit_taste = tk.StringVar()

search_frame = tk.LabelFrame(root, text="Search Options")

# Create and position widgets at the same time to save code space
lbl_name = ttk.Label(search_frame, text=f"Name:").grid(row = 0, column = 0)
lbl_colour = ttk.Label(search_frame, text=f"Colour:").grid(row = 1, column = 0)
lbl_taste = ttk.Label(search_frame, text=f"Taste:").grid(row = 2, column = 0)

# Since we want to use the config option to disable two of these widgets
# We can't position them at the same time, we have to position them like usual
en_name = ttk.Entry(search_frame, textvariable=edit_name)
en_colour = ttk.Entry(search_frame, textvariable=edit_colour)
en_taste = ttk.Entry(search_frame, textvariable=edit_taste)

button = ttk.Button(search_frame, text="Search", command=submit).grid(row = 3, column = 1, rowspan=2)

en_name.grid(row = 0, column = 1)
en_colour.grid(row = 1, column = 1)
en_taste.grid(row = 2, column = 1)

# TEMPORARY: Disable widgets
en_colour.config(state = "disabled")
en_taste.config(state = "disabled")

# END Search widgets
########################

########################
# Treeview code

def update_treeview(rows):
    global tree
    temp_list = []
    for member in rows:
        temp_list.append((member[0], member[1], member[2],member[3]))

    # Add the members to the treeview widget
    for row in temp_list:
        tree.insert("", tk.END, values = row)

# Place the treeview in it's own frame
tree_frame = tk.LabelFrame(root, text="Search Options")

# Create widget
tree = ttk.Treeview(tree_frame, columns = ["ID","Name", "Colour", "Taste"], show = 'headings')

# Set the headings
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Colour", text="Colour")
tree.heading("Taste", text="Taste")

tree.grid(row = 0, column = 0, sticky = "nsew")

# Add a scrollbar to our GUI
scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

# END Treeview code
########################

# Position the frames
search_frame.grid(column=0, row=0, padx=20, pady=20, sticky="ew")
tree_frame.grid(column=0, row=1, padx=20, pady=20, sticky="we")

root.mainloop()



########################################################
########################################################
# Build query here
    if(not edit_name.get()):      # Name was left blank, cancel
        return
    query = f"SELECT * FROM {table_name} WHERE Name = '{edit_name.get()}'"  

########################################################
# example COLLATE NOCASE
query = f"SELECT * FROM {table_name} WHERE Name = '{edit_name.get()}' COLLATE NOCASE"
#Adding ‘COLLATE NOCASE’ to the end of your query will instruct it to ignore case. 
#You can now search ‘apple’, ‘APPLE’, or even ‘aPpLe’, and you will get a result.


# example partial match
query = f"SELECT * FROM {table_name} WHERE Name LIKE '%{edit_name.get()}%' COLLATE NOCASE"

# Note: Remember to change the column name if you change the database. 
# Fruit uses ‘Name’ but the persons database has ‘First_Name’ and ‘Last_Name’.

# We place the % symbol on either side of the search term, and use ‘LIKE’ instead of the equal sign (=).
#If you search for ‘a’ in the fruit database, you will get results for apple, banana, and durian, plus any extras if you had added more rows.

#enabling and disabling widgets
# TEMPORARY: Disable widgets
en_colour.config(state = "disabled")
en_taste.config(state = "disabled")


# search for multiple terms
query = f"SELECT * FROM {table_name} WHERE Name = '{edit_name.get()}' AND Colour = '{edit_colour.get()}' COLLATE NOCASE"

# if you put ‘Apple into the name box and ‘Red’ into the colour box and search, you’ll find just one row that matches this exact search. 
#If we added more apples later that were green or yellow, we’d still only find red apples with this search term.

query = f"SELECT * FROM {table_name} WHERE (Taste = '{edit_taste.get()}' OR Colour = '{edit_colour.get()}') COLLATE NOCASE"

#Using the OR condition lets you search for whether either term is found. 
#You could search for fruit that is sweet or purple.
