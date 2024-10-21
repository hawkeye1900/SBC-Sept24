# ----------------------------
# Python Sets
# ----------------------------

# Sets in Python are collections of unique elements.
# They do not allow duplicate values and are unordered.

# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)  # Output: Set 1: {1, 2, 3, 4, 5}
print("Set 2:", set2)  # Output: Set 2: {4, 5, 6, 7, 8}

# ----------------------------
# Union of Sets
# ----------------------------

# Union combines elements from both sets, eliminating duplicates
union_set = set1 | set2
print("Union:", union_set)  # Output: Union: {1, 2, 3, 4, 5, 6, 7, 8}

# ----------------------------
# Intersection of Sets
# ----------------------------

# Intersection finds elements that are common to both sets
intersection_set = set1 & set2
print("Intersection:", intersection_set)  # Output: Intersection: {4, 5}

# ----------------------------
# Difference of Sets
# ----------------------------

# Difference finds elements that are in set1 but not in set2
difference_set = set1 - set2
print("Difference:", difference_set)  # Output: Difference: {1, 2, 3}

# ----------------------------
# Adding and Removing Elements
# ----------------------------

# Adding an element to a set
set1.add(9)
print("Set 1 after adding 9:", set1)  # Output: Set 1 after adding 9: {1, 2, 3, 4, 5, 9}

# Removing an element from a set
set1.remove(9)
print("Set 1 after removing 9:", set1)  # Output: Set 1 after removing 9: {1, 2, 3, 4, 5}

# ----------------------------
# Handling Non-Existent Elements
# ----------------------------

# Note: Removing an element that does not exist will raise a KeyError.
# Uncommenting the following line will cause an error
# set1.remove(10)  # KeyError: 10