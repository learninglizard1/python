# Filename: kg_convertor.py

# This module can be used generically to convert input from kg to another weight unit.
# We can expand this module to accommodate more weight conversions from kg to any other unit.
# This gives us a convenient place to define and maintain these.

def kg_to_lb(x):
    return x*2.205

def kg_to_stone(x):
    return x/6.35

def kg_to_gram(x):
    return x * 1000


# Filename: kg_main.py

# Import the file 'kg_convertor.py'
import kg_convertor

# Display some examples
print(kg_convertor.kg_to_gram(4))
print(kg_convertor.kg_to_lb(4))
print(kg_convertor.kg_to_stone(4))


#creating shorter names for the modules
#import kg_convertor as kg

#we can call out the functions using 'kg' alias

# example
# print (kg.kg_to_gram(5))
# print (kg.kg_to_lb(5))
# print (kg.kg_to_stone(5))