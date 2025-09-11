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

# A simple single purpose function that will perform just one query
# Gives you some benefits in that you can organise the data specifically
def insert_fruit(name, colour, taste):
    if(not name or not colour or not taste):
        # Perform some validation and error checking, be as thorough as you need to be
        return
    # Connect to the database
    conn = dbconnect()
    # Get the cursor object
    cursor = conn.cursor()
    # Run the query
    cursor.execute(f"INSERT INTO Fruit (Name,Colour,Taste) VALUES ('{name}','{colour}','{taste}');")
    # Commit changes
    conn.commit()
    # Close database
    cursor.close()

# Database functions END
########################

########################
# Our functions
def update_rows():
    # Get the rows from the query
    rows = select_query("SELECT * FROM Fruit;")

    # Display the results
    final_text = ""
    rows_found = len(rows)
    for row in rows:
        final_text += f"{row[0]} \t {row[1]} | {row[2]} | {row[3]} \n"
    # Update the widgets
    lbl_count.config(text=f"Total rows: {rows_found}")
    lbl_rows.config(text=final_text)

def submit():
    # Get the values from
    get_name = edit_name.get()
    get_colour = edit_colour.get()
    get_taste = edit_taste.get()

    # TODO: We should do some error checking here,
    # if there is blank data or such, warn the user with a messagebox and don't continue

    # Assumming everything has been validated by this point, insert the data
    query = f"INSERT INTO Fruit (Name,Colour,Taste) VALUES ('{get_name}','{get_colour}','{get_taste}');"
    execute_query(query)

    # Need to update the GUI interface, otherwise we will not see the change
    update_rows()

# END of our functions
######################

# Define variables
edit_name = tk.StringVar()
edit_colour = tk.StringVar()
edit_taste = tk.StringVar()

# Tkinter frames
left_frame = tk.LabelFrame(root, text="Display")
right_frame = tk.LabelFrame(root, text="Insert")

# Widgets
lbl_count = ttk.Label(left_frame, text=f"Total rows: 0")
lbl_rows = ttk.Label(left_frame, text="")

lbl_name = ttk.Label(right_frame, text=f"Name:")
lbl_colour = ttk.Label(right_frame, text=f"Colour:")
lbl_taste = ttk.Label(right_frame, text=f"Taste:")

en_name = ttk.Entry(right_frame, textvariable=edit_name)
en_colour = ttk.Entry(right_frame, textvariable=edit_colour)
en_taste = ttk.Entry(right_frame, textvariable=edit_taste)

button = ttk.Button(right_frame, text="Insert", command=submit)

# Position widgets
left_frame.grid(column=0, row=0, padx=20, pady=20)
right_frame.grid(column=1, row=0, padx=20, pady=20)

lbl_count.grid(row = 0, column = 0)
lbl_rows.grid(row = 1, column = 0)

lbl_name.grid(row = 0, column = 0)
lbl_colour.grid(row = 1, column = 0)
lbl_taste.grid(row = 2, column = 0)
en_name.grid(row = 0, column = 1)
en_colour.grid(row = 1, column = 1)
en_taste.grid(row = 2, column = 1)

button.grid(row = 3, column = 1, rowspan=2)

# When the program starts we need to update the rows at least once
update_rows()

# Tkinter loop
root.mainloop()
