"""
A list is a collection of items in a particular order. You can make a list that
includes the letters of the alphabet, the digits from 0 to 9, or the names of
all the people in your family.
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

"""
Accessing Elements in a List
Lists are ordered collections, so you can access any element in a list by
telling Python the position, or index, of the item desired.
"""
print(bicycles[0])
print(bicycles[3])

"""
Using Individual Values from a List
You can use individual values from a list just as you would any other variable. For example, you can use f-strings to create a message based on a
value from a list.
"""
message = f"My first bicycle was {bicycles[1].title()}"
print(message)

"""
3-1. Names: Store the names of a few of your friends in a list called names. Print
each person’s name by accessing each element in the list, one at a time.
"""
names = ['Bharath', 'Vinay', 'Mythri', 'Arpitha']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

"""
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the
person’s name
"""
message_to_friend = f"Hello, {names[2]}"
print(message_to_friend)

"""
3-3. Your Own List: Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.”
"""

car = ['Hyundai', 'Honda', 'Tata Nexon', 'Suzuki']
print(f"I would like to own a {car[2]} car.")