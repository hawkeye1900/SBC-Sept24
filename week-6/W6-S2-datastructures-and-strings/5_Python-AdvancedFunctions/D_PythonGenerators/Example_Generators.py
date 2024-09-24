# ----------------------------
# Python Generators
# ----------------------------

# Generators are a type of iterable, like lists or tuples, but they generate values on-the-fly and do not store them in memory.

# Basic Generator Example
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Using the generator
print("Counting up to 5:")
for number in count_up_to(5):
    print(number)
# Output:
# Counting up to 5:
# 1
# 2
# 3
# 4
# 5

# Generator Example with Manual Retrieval
generator = count_up_to(3)
print("\nManually retrieving values from generator:")
print(next(generator))  # Output: 1
print(next(generator))  # Output: 2
print(next(generator))  # Output: 3
# Uncommenting the following line will raise StopIteration
# print(next(generator))  # Raises StopIteration exception

# ----------------------------
# Comparison with Lists
# ----------------------------

# Generators are more memory-efficient compared to lists when dealing with large sequences.

# Example with a List
print("\nUsing a list to count up to 5:")
numbers_list = list(range(1, 6))
print(numbers_list)
# Output:
# [1, 2, 3, 4, 5]

# Example with a Generator
print("\nUsing a generator to count up to 5:")
for number in count_up_to(5):
    print(number)


# Generators are a powerful feature for handling large data sequences efficiently.
# They provide a convenient way to iterate over data without loading the entire dataset into memory.