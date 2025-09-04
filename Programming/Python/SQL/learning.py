
#CONNECTING TO A DATABASE
#
#
# Import SQLite3 module
import sqlite3

# Connect to the database, store access to this in a variable
# You can name this variable something else like db_connection for example
conn = sqlite3.connect("yourdatabase.db")

# <Our code that does stuff with the database>

# Close the database connection
# Just like when working with files, you want to close the 
# connection when we're done
conn.close()




#ERROR CHECKING CONNECTION TO A SQL DATABASE
#
# Import SQLite3 module and the SQLite3 error module
import sqlite3
from sqlite3 import Error

# Connect to the database, store access to this in a variable
def dbconnect():
    global conn
    try:
        # Attempt connection
        conn = sqlite3.connect("gym_database.db" )
    except Error as e:
        # Print the error message that appears
        print(e)
        return None         # Connection failed
    return conn             # Connection successful

# Define our program variables here
# We will use the database connection through the program
# so we want to make it a global
conn = None             # Set it to None by default since it hasn't connected yet

# Attempt to connect to database, this will also set conn if it's successful
# NOTE: We could also call this when defining conn if you wanted
if(not dbconnect()):
    # Connection to database failed, close the program
    print("Database connection failed")
    exit

# <Our code that does stuff with the database>

# Close the database connection
conn.close()





######IMPORTING CSV TO READ THE FILE

# Fruit CSV read and query

# Import CSV
import csv

# Open the file
try:
    with open("fruit.csv") as f:
        reader = csv.reader(f)
        for line in reader:
            query = f"""
                    INSERT INTO Fruit (
                    Name,
                    Colour,
                    Taste
                    )
                    VALUES (
                    '{line[0]}',
                    '{line[1]}',
                    '{line[2]}'
                    );
                    """
            print(query)
except:
    print("An error occurred reading the file")
#
#
#
# IMPORTING FROM A CSV FILE

import sqlite3
from sqlite3 import Error
import csv

def dbconnect():
    global conn
    try:
        conn=sqlite3.connect("peoples.db")
    except Error as e:
        print (e)
        return None
    return conn

conn = None

if (not dbconnect()):
    print ("Failed to connect to the database. Exiting program.")
    exit()



c= conn.cursor()

query = """
CREATE TABLE IF NOT EXISTS People(
    ID INTEGER PRIMARY KEY,
    First_Name TEXT NOT NULL,
    Last_Name TEXT NOT NULL,
    Gender TEXT NOT NULL,
    Age INTEGER NOT NULL,
    Email TEXT NOT NULL,
    Phone TEXT NOT NULL,
    Occupation TEXT NOT NULL,
    Martial_Status TEXT NOT NULL,
    Number_of_Children INTEGER NOT NULL
)
"""
c.execute(query)

csv_file = 'persons.csv'

with open(csv_file, 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        c.execute("""
            INSERT INTO people (First_Name, Last_Name, Gender, Age, Email, Phone, Occupation, Martial_Status, Number_of_Children)
            VALUES
                  ( ?, ?, ?, ?, ?, ?, ?, ?, ?)
                  
        """, row)

conn.commit()
conn.close()




