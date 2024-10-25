# ----------------------------
# Python Error Handling and Exceptions
# ----------------------------

# 1. Basic Try-Except Example
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")

# 2. Handling Multiple Exceptions
try:
    number = int("Step8up")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# 3. Using Finally to Execute Code Regardless of an Exception
try:
    file = open("test.txt", "r")
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("This will always execute.")

# 4. Using Else Block
try:
    number = 5
    result = number / 2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"The result is {result}.")

# 5. Raising Custom Exceptions
age = -1
if age < 0:
    raise ValueError("Age cannot be negative!")

# 6. Catching All Exceptions (Not Recommended for Broad Use)
try:
    result = 10 / 0
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# 7. Custom Exceptions Example
class CustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print(f"CustomError: {e.message}")

# 8. Exception Example with Detailed Logging
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # This will raise an IndexError
except IndexError:
    print("Error: Index out of range.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# ----------------------------
# Python Classes and Objects
# ----------------------------

# 1. Defining a Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

    def get_age(self):
        return f"{self.name} is {self.age} years old."

# 2. Creating Objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# 3. Accessing Attributes and Methods
print("Dog 1 details:")
print(dog1.get_age())  # Output: Buddy is 3 years old.
print(dog1.bark())     # Output: Buddy says woof!

print("\nDog 2 details:")
print(dog2.get_age())  # Output: Max is 5 years old.
print(dog2.bark())     # Output: Max says woof!

# 4. Modifying Attributes
dog1.age = 4
print("\nUpdated Dog 1 details:")
print(dog1.get_age())  # Output: Buddy is 4 years old.