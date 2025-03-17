"""
Strings is one of the fundamental datatypes in python. Strings are used to represent text data.
We say that strings are a fundamental data type because they can’t be broken down into smaller values of a different type.
"""

print(type("Welcome to Python Learning"))  # < 'str' >

# Assigning string to variable
phrase = "Hello, World!"
print(type(phrase))  # < 'str' >

"""
You can use either single quotes (string1) or double quotes (string2)
to create a string as long as you use the same type at the beginning
and end of the string.
"""

# String Literal
string1 = 'Hello, World!'
string2 = "Hello, World!"

"""
The quotes surrounding a string are called delimiters because they
tell Python where a string begins and where it ends. 
"""
string3 = "We're One"
string4 = 'I said "Put down the phone!!"'

# Determine length of a string
print(len("abc"))  # 3

# --------------------------------------------------------------------------- #
"""
1. Concatenation, which joins two strings together
2. Indexing, which gets a single character from a string
3. Slicing, which gets several characters from a string at once
"""

first_name = "Alan"
second_name = "Walker"
concatenated_string = first_name + " " + second_name
print(concatenated_string)

# Indexing - Each string has a numbered position called 'index'
flavor = "apple pie"
print(flavor[0])
print(flavor[2])

print(flavor[-2])

# Slicing if you want the first 3 letters You could access each character by index and concatenate them
first_three_letters = flavor[0] + flavor[1] + flavor[2]

# Alternative way - You can extract a portion of a string, called a substring, by inserting a colon
# between two index numbers inside of square brackets

print(flavor[0:3])
print(flavor[:5]) # omitting first index - python assumes as it's starts with 0
print(flavor[5:]) # omitting last index - python assumes it's a last index
print(flavor[:]) # omitting both index - python assumes as an entire string

# 4.4 - Interact With User Input
prompt = "Hello, What's up?"
user_input = input(prompt)
print("You Said:", user_input)
