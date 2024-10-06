# ----------------------------
# Python Classes and Objects
# ----------------------------

# 1. Defining a Class
# A class represents a blueprint for creating objects with specific attributes and methods.

# Define a class named `Dog`
class Dog:
    # The `__init__` method is a special method that is called when a new object is created.
    # It initializes the object's attributes.
    def __init__(self, name, age):
        # `self` refers to the instance of the class.
        # `name` and `age` are attributes that will be set when an object is created.
        self.name = name  # Assign the value of the name parameter to the `name` attribute
        self.age = age    # Assign the value of the age parameter to the `age` attribute
    
    # Define a method named `bark` that belongs to the Dog class
    def bark(self):
        # This method returns a string that says the dog is barking
        return f"{self.name} says woof!"
    
    # Define a method named `get_age` that returns the dog's age
    def get_age(self):
        # This method returns a string with the dog's name and age
        return f"{self.name} is {self.age} years old."

# 2. Creating Objects
# Instantiate (create) objects of the Dog class with specific attributes

# Create an object named `dog1` with the name "Buddy" and age 3
dog1 = Dog("Buddy", 3)
# Create another object named `dog2` with the name "Max" and age 5
dog2 = Dog("Max", 5)

# 3. Accessing Attributes and Methods
# Use the methods and attributes of the objects and print the results

# Print details for `dog1`
print("Dog 1 details:")
# Call the `get_age` method for `dog1` and print the result
print(dog1.get_age())  # Output: Buddy is 3 years old.
# Call the `bark` method for `dog1` and print the result
print(dog1.bark())     # Output: Buddy says woof!

# Print details for `dog2`
print("\nDog 2 details:")
# Call the `get_age` method for `dog2` and print the result
print(dog2.get_age())  # Output: Max is 5 years old.
# Call the `bark` method for `dog2` and print the result
print(dog2.bark())     # Output: Max says woof!

# 4. Modifying Attributes
# Change the age attribute of `dog1` and print the updated details

# Modify the `age` attribute of `dog1` to 4
dog1.age = 4
print("\nUpdated Dog 1 details:")
# Call the `get_age` method for the updated `dog1` and print the result
print(dog1.get_age())  # Output: Buddy is 4 years old.

# Classes are fundamental in object-oriented programming.
# They allow you to model real-world entities with attributes and behaviors.