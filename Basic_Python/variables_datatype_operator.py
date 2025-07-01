# Day 1: Variables, Data Types & Operators

# 1. Variables
name = "Alice"
age = 30
height = 1.75
is_student = True

# 2. Data Types
num_int = 10         # int
num_float = 20.5     # float
my_string = "Hello, Python!" # str
is_active = True     # bool

print(type(num_int))    # Output: <class 'int'>
print(my_string + " How are you?") # Output: Hello, Python! How are you?
print(f"My name is {name} and I am {age} years old.")

# 3. Operators
x = 10
y = 3

print(x + y)    # 13
print(x / y)    # 3.333...
print(x // y)   # 3
print(x % y)    # 1

print(x > y)    # True
print(x == 10)  # True
print(x != y)   # True

print(True and False) # False
print(True or False)  # True
print(not True)       # False