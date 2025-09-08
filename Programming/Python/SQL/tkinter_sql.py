# Import modules
import sqlite3
from sqlite3 import Error
import tkinter as tk
from tkinter import ttk

# Tkinter setup
root = tk.Tk()
root.geometry("600x250")

# The path/name of our database file
# It is convenient to keep it somewhere easy to see and edit
database_path = "fruit.db"

####################
# Database functions

# Connects to the database, returns the database object
#The dbconnect() is almost the same as before but we don’t use a global scope variable anymore, we just return the database object.

def dbconnect():
    conn = None
    try:
        conn = sqlite3.connect(database_path)
    except Error as e:
        print(e)
        return None
    return conn

# Executes a query
# We can use this for insert, update, and delete
# It will not work for select since we need to get the rows
#The execute_query() function is intended for our insert, update, and delete interactions. It has the commit() function that these require.
def execute_query(query):
    # Connect to the database
    conn = dbconnect()
    # Get the cursor object
    cursor = conn.cursor()
    # Run the query
    cursor.execute(query)
    # Commit changes
    conn.commit()
    # Close database
    cursor.close()

#the select_query() is used when we want to get data. It will return the rows when we provide a query.
def select_query(query):
     # Connect to the database
    conn = dbconnect()
    # Get the cursor object
    cursor = conn.cursor()
    # Run the query
    cursor.execute(query)
    rows = cursor.fetchall()
    # Close database
    cursor.close()
    # Return the rows we obtained
    return rows

# Database functions END
########################

rows = select_query("SELECT * FROM Fruit;")
# Print the rows we found
final_text = ""
rows_found = len(rows)
for row in rows:
    final_text += f"{row[0]} \t {row[1]} | {row[2]} | {row[3]} \n"

lbl_count = ttk.Label(root, text=f"Total rows: {rows_found}")
lbl_rows = ttk.Label(root, text=final_text)

lbl_count.grid(row = 0, column = 0)
lbl_rows.grid(row = 1, column = 0)

# Tkinter loop
root.mainloop()




##########################################
#using treeview to show the fruit database

import sqlite3
from sqlite3 import Error
import tkinter as tk
from tkinter import ttk

# Tkinter setup
root = tk.Tk()
root.geometry("600x300")
root.title("Fruit Database")

# Database path
database_path = "fruit.db"

####################
# Database functions

def dbconnect():
    try:
        return sqlite3.connect(database_path)
    except Error as e:
        print(e)
        return None

def execute_query(query):
    conn = dbconnect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def select_query(query):
    conn = dbconnect()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

# Database functions END
########################

# Get data from database
rows = select_query("SELECT * FROM Fruit;")
rows_found = len(rows)

# Set up the Treeview
tree = ttk.Treeview(root, columns=("ID", "Name", "Color", "Taste"), show='headings')

# Define columns
tree.heading("ID", text= "ID")
tree.heading("Name", text="Name")
tree.heading("Color", text="Color")
tree.heading("Taste", text="Taste")

# Optionally configure column widths
tree.column("ID", width= 50)
tree.column("Name", width=150)
tree.column("Color", width=150)
tree.column("Taste", width=150)

for row in rows:
    tree.insert("", "end", values=( row [0], row[1], row[2], row[3]))

# Pack or grid the treeview
tree.grid(row=1, column=0, padx=5, pady=5)

#row count
lbl_count = tk.Label(root, text=f"Total rows: {rows_found}")
lbl_count.grid(row=0, column=0, sticky="w", padx=10, pady=5)

# Add a scrollbar to our GUI
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=1, sticky='ns')


root.mainloop()

