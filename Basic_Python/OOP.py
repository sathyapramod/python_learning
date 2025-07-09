# Class: A blueprint or a template for creating objects. It defines the common attributes and methods that all objects of that type will have. (e.g., "Car" is a class)
# Object (Instance): An individual instance of a class. A concrete realization of the blueprint. (e.g., "my_red_Honda" is an object of the Car class).

# Class definition
class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Construct Method
    def __init__(self, name, breed, age):
        # Instance attributes
        self.name = name
        self.breed = breed
        self.age = age

    # Instance Method
    def bark(self):
        print(f"{self.name} says Woof!")

    def description(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}."

# Creating Objects
dog1 = Dog("Buddy", "Golden Retriever", 5)
dog2 = Dog("Lucy", "Labrador", 3)

print(f"{dog1.name} is a {dog1.species}.")
print(f"{dog2.name} is {dog2.age} years old.")

# Calling Method
dog1.bark()
print(dog2.description())

# Key OOP Principles
# Encapsulation
# Inheritance
# Polymorphism
# Abstraction

## Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplemented("Subclass must implement abstract method")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return f"{self.name} says Meow!"

    def display_color(self):
        return f"{self.name} is a {self.color} cat."

my_cat = Cat("Whiskers", "black")
print(my_cat.speak())
print(my_cat.display_color())
