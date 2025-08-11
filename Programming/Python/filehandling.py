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


