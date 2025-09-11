# Import modules 
import sqlite3 
from sqlite3 import Error 
import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox 
 
 
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
 
 
    # TODO: We should do some error checking here, 
    # if there is blank data or such, warn the user with a messagebox and don't continue 
 
 
    # WARNING: Always warn the user when they're about to remove data 
    # Give them a chance to cancel in case an error was made 
    if(not messagebox.askokcancel("Delete", f"Are you sure you wish to delete the row for {get_name}")): 
        return 
 
 
    # Assumming everything has been validated by this point, insert the data 
    query = f"DELETE FROM Fruit WHERE Name = '{get_name}'" 
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
 
 
en_name = ttk.Entry(right_frame, textvariable=edit_name) 
  

button = ttk.Button(right_frame, text="Delete", command=submit) 
  

# Position widgets 
left_frame.grid(column=0, row=0, padx=20, pady=20) 
right_frame.grid(column=1, row=0, padx=20, pady=20) 
 
 
lbl_count.grid(row = 0, column = 0) 
lbl_rows.grid(row = 1, column = 0) 
 
 
lbl_name.grid(row = 0, column = 0) 
en_name.grid(row = 0, column = 1) 
 
 
button.grid(row = 3, column = 1, rowspan=2) 
 
 
 
# When the program starts we need to update the rows at least once 
update_rows() 
 
 
 
# Tkinter loop 
root.mainloop()
