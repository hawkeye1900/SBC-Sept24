# ----------------------------
# Python Error Handling and Exceptions
# ----------------------------

# 1. Basic Try-Except Example

# Attempting to divide by zero will raise a ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
# Output:
# Error: You cannot divide by zero!


# 2. Handling Multiple Exceptions

# Example: Converting a string to an integer might raise a ValueError
try:
    number = int("Step8up")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
# Output:
# Error: invalid literal for int() with base 10: 'Step8up'


# 3. Using Finally to Execute Code Regardless of an Exception

try:
    file = open("test.txt", "r")
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("This will always execute, whether an exception occurs or not.")
# Output (if file does not exist):
# Error: File not found.
# This will always execute, whether an exception occurs or not.


# 4. Using Else Block

# The else block is executed if no exceptions are raised in the try block
try:
    number = 5
    result = number / 2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"The result is {result}.")
# Output: The result is 2.5


# 5. Raising Custom Exceptions

# Example: Checking if age is a valid number and raising a ValueError if not
age = -1
if age < 0:
    raise ValueError("Age cannot be negative!")
# Output:
# Traceback (most recent call last):
#   ...
# ValueError: Age cannot be negative!


# 6. Catching All Exceptions (Not Recommended for Broad Use)

# Be cautious when catching all exceptions with a broad 'except' clause
try:
    result = 10 / 0
except Exception as e:
    print(f"An unexpected error occurred: {e}")
# Output:
# An unexpected error occurred: division by zero


# 7. Custom Exceptions Example

# You can define your own exceptions by inheriting from the Exception class. Classes topic is discussed later in the series.
class CustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print(f"CustomError: {e.message}")
# Output: CustomError: This is a custom error.


# 8. Exception Example with Detailed Logging

# Example: Use more specific exception handling to log detailed errors
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # This will raise an IndexError
except IndexError:
    print("Error: Index out of range.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
# Output: Error: Index out of range.


# 9. Important: Best Practices

# Use specific exceptions when possible.
# Avoid using broad 'except' clauses as it can hide other issues.

# Error Handling is an important feature in Python to manage errors gracefully and ensure your code doesn't crash unexpectedly.