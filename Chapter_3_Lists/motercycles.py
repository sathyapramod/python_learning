"""
Modifying, Adding, and Removing Elements
"""

# Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

print(motorcycles[0])

motorcycles[0] = 'ducati'
print(motorcycles)

# Adding Elements to a List
# Appending Elements to the End of a List -- "The simplest way to add a new element to a list is to append the item to the
# list. When you append an item to a list, the new element is added to the end
# of the list."

motorcycles.append('honda')
print(motorcycles)

# The append() method makes it easy to build lists dynamically. For example,
# you can start with an empty list and then add items to the list using a series
# of append() calls.

cars = []
cars.append('hyundai')
cars.append('nexa')
cars.append('tata')
cars.append('suzuki')
print(cars)

# Inserting Elements into a List
# You can add a new element at any position in your list by using the insert()
# method. Below example we insert the item at the beginning of the list.

cars.insert(0, 'kia')
print(cars)

# Removing Elements from a List
# Removing an Item Using the del Statement - If you know the position of the item you want to remove from a list, you can
# use the del statement.

# Here we use the del statement to remove the first item, 'honda', from the list of motorcycles
del motorcycles[3]
print(motorcycles)

del motorcycles[0]
print(motorcycles)  # Removing ducati

# Removing an Item Using the pop() Method
# The pop() method removes the last item in a list

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
