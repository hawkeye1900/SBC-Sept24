# ----------------------------
# Python Iterators, Comprehensions, and Loops
# ----------------------------

# =============================
# 1. Python Iterators
# =============================

# Basic Iterator Example with Lists
my_list = [10, 20, 30, 40, 50]
iterator = iter(my_list)

# Retrieve elements using next()
print("Iterating through the list:")
print(next(iterator))  # Output: 10
print(next(iterator))  # Output: 20
print(next(iterator))  # Output: 30

# Using a for loop with an iterator
print("\nUsing a for loop to iterate through the list:")
for item in my_list:
    print(item)

# Iterating over Strings
my_string = "Step8up"
string_iterator = iter(my_string)

print("\nManually iterating through the string:")
print(next(string_iterator))  # Output: S
print(next(string_iterator))  # Output: t

# Handling StopIteration
print("\nHandling StopIteration with try-except:")
try:
    while True:
        print(next(iterator))
except StopIteration:
    print("Reached the end of the list.")

# =============================
# 2. Python Comprehensions
# =============================

# List Comprehensions
squares = [x**2 for x in range(1, 6)]
print("\nList of squares:", squares)  # Output: [1, 4, 9, 16, 25]

# Filtering a list: even numbers from 1 to 10
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("List of even numbers:", even_numbers)  # Output: [2, 4, 6, 8, 10]

# Set Comprehensions
unique_squares = {x**2 for x in range(1, 6)}
print("Set of unique squares:", unique_squares)  # Output: {1, 4, 9, 16, 25}

# Dictionary Comprehensions
square_dict = {x: x**2 for x in range(1, 6)}
print("Dictionary of numbers and their squares:", square_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# =============================
# 3. Python Loops
# =============================

# For Loop with Lists
fruits = ["apple", "banana", "cherry"]
print("\nFruits list:")
for fruit in fruits:
    print(fruit)

# For Loop with Tuples
numbers = (1, 2, 3, 4, 5)
print("\nNumbers tuple:")
for number in numbers:
    print(number)

# For Loop with Ranges
print("\nRange from 0 to 4:")
for i in range(5):
    print(i)

# While Loop
count = 1
print("\nCounting with while loop:")
while count <= 3:
    print(count)
    count += 1

# Break Statement
print("\nLoop with break statement:")
for i in range(5):
    if i == 3:
        break
    print(i)

# Continue Statement
print("\nLoop with continue statement:")
for i in range(5):
    if i % 2 == 0:
        continue
    print(i)

# Loops are essential for repeating tasks and iterating over sequences.
# They help in efficiently processing data and controlling the flow of execution.