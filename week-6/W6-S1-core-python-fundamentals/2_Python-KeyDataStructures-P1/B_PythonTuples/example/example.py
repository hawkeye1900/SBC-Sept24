# ----------------------------
# Python Tuples
# ----------------------------

# Tuples in Python are immutable sequences of values.
# This means once a tuple is created, its elements cannot be changed.

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)

# ----------------------------
# Accessing Tuple Elements
# ----------------------------

# Accessing elements using index
print("First Element:", my_tuple[0])  # Output: First Element: 1
print("Last Element:", my_tuple[-1])  # Output: Last Element: 5

# ----------------------------
# Slicing a Tuple
# ----------------------------

# Slicing creates a new tuple from a portion of the original tuple
sub_tuple = my_tuple[1:4]  # Get elements from index 1 to 3 (inclusive of 1, exclusive of 4)
print("Sliced Tuple (index 1 to 3):", sub_tuple)  # Output: Sliced Tuple (index 1 to 3): (2, 3, 4)

# ----------------------------
# Immutable Nature of Tuples
# ----------------------------

# Tuples are immutable, so trying to change an element will raise an error
# Uncommenting the following line will cause an error
# my_tuple[1] = 10  # TypeError: 'tuple' object does not support item assignment

# ----------------------------
# Comparison with Lists
# ----------------------------

# Lists are mutable sequences
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

# Lists can be changed
my_list[1] = 10
print("Modified List:", my_list)  # Output: Modified List: [1, 10, 3, 4, 5]

# ----------------------------
# Key Differences
# ----------------------------

# Tuples are generally used for fixed collections of items,
# whereas lists are used for collections that can change.