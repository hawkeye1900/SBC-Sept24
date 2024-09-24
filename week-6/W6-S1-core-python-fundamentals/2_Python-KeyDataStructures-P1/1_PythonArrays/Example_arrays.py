# ----------------------------
# Python Arrays (Lists)
# ----------------------------

# Arrays in Python are implemented as lists. They are mutable sequences that can store a collection of items.

# Initializing an array (list) with sample values
my_array = [1, 2, 3, 4, 5]  # List of integers
print("Initial Array:", my_array)

# ----------------------------
# Accessing Elements
# ----------------------------

# Accessing elements using index
first_element = my_array[0]   # Index 0 corresponds to the first element
third_element = my_array[2]   # Index 2 corresponds to the third element

print("First Element:", first_element)
print("Third Element:", third_element)

# ----------------------------
# Updating Elements
# ----------------------------

# Modifying elements at a specific index
my_array[1] = 10  # Update the second element to 10

print("Array after update:", my_array)

# ----------------------------
# Slicing the Array
# ----------------------------

# Slicing creates a new list from a portion of the original list
sub_array = my_array[1:4]  # Get elements from index 1 to 3 (inclusive of 1, exclusive of 4)

print("Sub-array (Slice):", sub_array)

# ----------------------------
# Adding and Removing Elements
# ----------------------------

# Adding elements to the end of the array
my_array.append(6)  # Append 6 to the end of the array

# Removing elements from the array
my_array.remove(10)  # Remove the first occurrence of 10 from the array

print("Array after modifications:", my_array)

# ----------------------------
# Example Usage of Array Operations
# ----------------------------

# Display the final state of the array and the results of operations
print("Final Array:", my_array)