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

