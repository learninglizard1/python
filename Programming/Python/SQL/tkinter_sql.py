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
