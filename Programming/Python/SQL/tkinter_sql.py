import sqlite3
from sqlite3 import Error
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("650x250")


database_path = "fruit.db"


def dbconnect():  #The dbconnect() is almost the same as before but we don’t use a global scope variable anymore, we just return the database object.

    conn = None
    try:
        conn = sqlite3.connect(database_path)
    except Error as e:
        print (e)
        return None
    return conn

def execute_query(query): #The execute_query() function is intended for our insert, update, and delete interactions. It has the commit() function that these require.
    #connect to the database
    conn = dbconnect()
    #get the cursor object
    cursor = conn.cursor()
    #run the query
    cursor.execute(query)
    #commit changes
    conn.commit()
    #close database
    conn.close()

def select_query(query): #the select_query() is used when we want to get data. It will return the rows when we provide a query.
    #connect to the database
    conn = dbconnect()
    #get the cursor object
    cursor = conn.cursor()
    #run the query
    cursor.execute(query)
    rows= cursor.fetchall()
    #close databse
    conn.close()
    #return the rows we obtained
    return rows




rows = select_query("SELECT * FROM Fruit;")

#print the rows we found
final_text=""
rows_found= len(rows)
for row in rows:
    final_text += f"{row[0]} \t {row[1]} | {row[2]} | {row[3]} \n"


lbl_count = ttk.Label(root, text= f"Total rows: {rows_found}")
lbl_rows = ttk.Label(root, text=final_text)

lbl_count.grid(row=0, column=0)
lbl_rows.grid(row=1, column=0)

root.mainloop()
