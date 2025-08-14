#LEARNING HOW TO OPEN A FILE USING PYTHON ( reading and writing)

# Read file example

import os

file_path = ".\\information.txt"

# Open our file
with open(file_path,"r") as f:
    # Use the read() function and set the results to the all_content variable
    all_content = f.read()
    # Print our results
    print(all_content)



# Using UTF-8 encoding

import os

file_path = ".\\information.txt"

# Using extra parameter encoding with UTF-8 to ensure the file is readable
with open(file_path, "r", encoding="UTF-8") as f:
    all_content = f.read()
    print(all_content)


# Read file example - Display first 20 characters

import os

file_path = ".\\information.txt"

# Open the file in read-only mode
with open(file_path, "r") as f:
    # Read the first 20 characters of the file
    some_content = f.read(20)
    # Output our text 
    print(some_content)



# Readline example

# Imports
import os
import time

file_path = ".\\information.txt"

with open(file_path, "r", encoding="UTF-8") as f:
    # Print the first line
    print(f.readline())
    # Print the second line
    print(f.readline())
    # Print the third line
    print(f.readline())


# Readline example

# Imports
import os
import time

file_path = ".\\information.txt"

with open(file_path, "r", encoding="UTF-8") as f:
    # Loop through each line in the file
    for line in f:
        print(line)





# Readlines example

# Imports
import os
import time

file_path = ".\\information.txt"

with open(file_path, "r", encoding="UTF-8") as f:
    # Read all lines and store as a list
    list_of_lines = f.readlines()

    # Loop through our list
    for line in list_of_lines:
        # For each iteration, print the line string
        print(line)

        # Delay for 0.2 seconds
        # This is a function from the time module
        time.sleep(0.2)





#reversing the line example
#imports 
import os
import time

file_path = ".\\education_journey.txt"

with open(file_path, "r", encoding= "UTF-8") as f:
    reading = f.readlines()

    for read in reading [::-1]: #or you can use for read in reversed(reading):
        print(read)





# Write file example

# Import os the same as with reading
import os

file_path = ".\\education_journey.txt"

# Open the file: this will create a new file with this name or overwrite if it exists
# Notice the "w" for write
with open(file_path, "w") as f:
    f.write("Hello everyone!")
    f.write("What a lovely day")

# Append to an existing file
# Notice the "a" for append is used instead of "w"
with open(file_path, "a") as f:
    f.write("It would be nice to go for a walk")
    f.write("Maybe I should take my bike!")

# Open the file to read and show the contents of the file
with open(file_path, "r") as f:
    print(f.read())



# Writelines example

import os

file_path = ".\\example.txt"

some_lines = ["Apple\n", "Banana\n", "Carrot\n", "Daffodil\n", "Elderberry\n"] #adding \n to start in a new line

# Write a new file using "w"
with open(file_path, "w") as f:
    f.writelines(some_lines)

# Open the file to read and show the contents of the file
with open(file_path, "r") as f:
    print(f.read())




#exception handling with files
import os

file_path = ".\\information.txt"

# Try...except example
try:
    # Any code placed in the try will attempted to run
    # If an error is found, run the code in except and show an error
    with open(file_path, "r", encoding="UTF-8") as f:
        print(f.read())
except:
    # An error has occurred, display a message to the user
    print("Error: File does not exist")






#--------------------------WORKING WITH CSV FILES ----------------------------------
#
#
#
#Example 1
# Working with CSV

# Imports
import os
import csv      # Include csv to allow useful functions for csv files

file_path = ".\\biostats.csv"

# Open file to read as we have normally done so far
with open(file_path, "r") as f:
    # Print as a normal text file
    print(f.read())

# Note: the file will have closed since the block has ended

# Open file again in read mode like usual
with open(file_path, "r") as f:
    # This time we use the csv reader function to open it
    # Note: The variable name can be anything
    our_csv_file = csv.reader(f)

    # Print all the rows in our file
    for row in our_csv_file:
        # The row will show a list of the items in the row
        print(row)




#example 2
# Working with CSV

import os
import csv

file_path = ".\\biostats.csv"

# Open file again in read mode like usual
with open(file_path, "r") as f:
    # This time we use the csv reader function to open it
    our_csv_file = csv.reader(f)

    # Print only the first column - name
    for row in our_csv_file:
        print(row[0]) 

# NOTE: You will encounter an error "list index out of range"
# This occurs because the biostats.csv file has blank entries at the end of the file



#to eliminate error and skip empty lines
# Working with CSV

import os
import csv

file_path = ".\\biostats.csv"

# Open file again in read mode like usual
with open(file_path, "r") as f:
    # This time we use the csv reader function to open it
    our_csv_file = csv.reader(f)

    # Print only the first column - name
    for row in our_csv_file:
        if(len(row) <= 0):
            continue
        print(row[0])



###writing in csv file####
#
#
# Working with CSV

import os
import csv

file_path = ".\\biostats.csv"

# Remember to use the "a" when appending data
with open(file_path, "a") as f:
    # You don't have to specify a delimiter since comma is the default but you can if you want to
    CSV = csv.writer(f, delimiter=',') 
    CSV.writerow(['John', 'M', 29, 71, 176])
    CSV.writerow(['Mary', 'F', 28, 65, 131])




#using csv as a dictionary

# Working with CSV

import os
import csv

file_path = ".\\new_biostats.csv"

# Remember to use the "w" when creating a new file
with open(file_path, "w") as f:
    # Define our column names, you can use single or double quotes like any string
    keys = ['Name','Gender','Age','Height (in)','Weight (lbs)']
    # Create a variable and use the DictWriter() function
    # You can name the variable anything, CSV is used here for convenience
    # fieldnames=keys is the parameter to use the list we defined earlier as the column names
    CSV = csv.DictWriter(f, fieldnames=keys)
    # Add column names in the CSV file first
    CSV.writeheader() 
    # Write two new rows to the file
    CSV.writerow({'Name': 'Joes', 'Gender':'M', 'Age':29, 'Height (in)':71, 'Weight (lbs)': 176})
    CSV.writerow({'Name': 'Blog', 'Gender':'F', 'Age':28, 'Height (in)':65, 'Weight (lbs)': 131})



#
# Writing to a file to create a CSV 
#
import os 

 
file_path = ".\\example.txt" 

 
# Write a new file using "w" 
with open(file_path, "w") as f: 
    # We simply write to the file like normally, except we just add 
    # the comma in where we need it, creating a CSV file we can use later 
    # You can break it up like this or write parts or the whole line at once 
    f.writelines("John,") 
    f.writelines("Smith,") 
    f.writelines("23,") 
    f.writelines("Hamilton,") 
    f.writelines("555-3958") 
 

#  output = John,Smith,23,Hamilton,555-3958


