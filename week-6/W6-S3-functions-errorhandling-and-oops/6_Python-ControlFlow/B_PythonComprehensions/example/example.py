# ----------------------------
# Python Comprehensions
# ----------------------------

# 1. List Comprehensions

# Creating a list of squares from 1 to 5 using a for loop
squares = [x**2 for x in range(1, 6)]
print("List of squares:", squares)
# Output: [1, 4, 9, 16, 25]

# Filtering a list: create a list of even numbers from 1 to 10
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("List of even numbers:", even_numbers)
# Output: [2, 4, 6, 8, 10]

# 2. Set Comprehensions

# Creating a set of unique square values using set comprehension
unique_squares = {x**2 for x in range(1, 6)}
print("Set of unique squares:", unique_squares)
# Output: {1, 4, 9, 16, 25}

# 3. Dictionary Comprehensions

# Creating a dictionary that maps numbers to their squares
square_dict = {x: x**2 for x in range(1, 6)}
print("Dictionary of numbers and their squares:", square_dict)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Example of filtering in a dictionary comprehension: only include numbers that are even
filtered_square_dict = {x: x**2 for x in range(1, 6) if x % 2 == 0}
print("Filtered dictionary of even numbers and their squares:", filtered_square_dict)
# Output: {2: 4, 4: 16}

# Comprehensions provide a concise and readable way to work with lists, sets, and dictionaries.
# They are great for transforming or filtering data in one line.