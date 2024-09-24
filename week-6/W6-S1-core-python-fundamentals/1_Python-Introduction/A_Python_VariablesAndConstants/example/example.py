# variables_and_constants.py

# ----------------------------
# Python Variables and Constants
# ----------------------------

# Variables in Python can store data of different types and can be changed during program execution.

# String variable
name = "Alice"  # Stores a sequence of characters
print("Name:", name)

# Integer variable
age = 25  # Stores whole numbers
print("Age:", age)

# Float variable
height = 5.5  # Stores decimal numbers
print("Height:", height)

# Boolean variable
is_student = True  # Stores True or False values
print("Is Student:", is_student)

# ----------------------------
# Constants in Python
# ----------------------------

# Python doesn't have built-in constant types, but by convention, we use uppercase variable names to indicate constants.

PI = 3.14159      # Mathematical constant for Pi
GRAVITY = 9.8     # Acceleration due to gravity on Earth in m/s^2

print("Value of PI:", PI)
print("Value of GRAVITY:", GRAVITY)

# ----------------------------
# Mutable vs Immutable Data Types
# ----------------------------

# Immutable data types cannot be changed after they are created.
# Examples: int, float, str, tuple

# Mutable data types can be changed after they are created.
# Examples: list, dict, set

# Immutable example with an integer
original_number = 10
print("Original Number:", original_number)

# Attempting to change the integer actually creates a new object
original_number += 5
print("Modified Number:", original_number)

# Mutable example with a list
fruits = ["apple", "banana", "cherry"]
print("Original List:", fruits)

# Modifying the list (mutable)
fruits.append("orange")
print("Modified List:", fruits)

# ----------------------------
# Example Usage of Variables and Constants
# ----------------------------

# Calculating the area of a circle using the constant PI
circle_radius = 10  # Variable storing the radius of the circle
circle_area = PI * (circle_radius ** 2)  # Area formula: πr^2

print(f"The area of a circle with radius {circle_radius} is {circle_area}")

# ----------------------------
# Proper Naming Conventions
# ----------------------------

# Variable names should be descriptive and use lowercase letters, with words separated by underscores (snake_case)
first_name = "Alice"
last_name = "Smith"

# Constants are usually defined at the top of the file and use uppercase letters with underscores
MAX_USERS = 100

print("First Name:", first_name)
print("Last Name:", last_name)
print("Maximum Users Allowed:", MAX_USERS)