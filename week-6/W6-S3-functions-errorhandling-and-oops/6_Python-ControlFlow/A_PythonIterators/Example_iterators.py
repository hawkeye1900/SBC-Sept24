# ----------------------------
# Python Iterators
# ----------------------------

# 1. Basic Iterator Example with Lists

# A list is an iterable, meaning we can get an iterator from it using the iter() function.
my_list = [10, 20, 30, 40, 50]
iterator = iter(my_list)

# We can manually retrieve elements using the next() function.
print(next(iterator))  # Output: 10
print(next(iterator))  # Output: 20
print(next(iterator))  # Output: 30

# You can keep calling next() until the iterator is exhausted.
# Uncomment the next line to raise StopIteration when the iterator is exhausted:
# print(next(iterator))  # Raises StopIteration

# 2. Using a for Loop with an Iterator

# Python automatically creates an iterator when using a for loop, so there's no need to manually call iter() and next().
print("\nUsing a for loop to iterate through the list:")
for item in my_list:
    print(item)
# Output:
# 10
# 20
# 30
# 40
# 50

# 3. Iterating over Strings

# Strings are also iterables, so we can create an iterator for a string using iter().
my_string = "Step8up"
string_iterator = iter(my_string)

# Manually retrieve the characters using next().
print("\nManually iterating through the string:")
print(next(string_iterator))  # Output: S
print(next(string_iterator))  # Output: t
print(next(string_iterator))  # Output: e

# 4. Handling StopIteration

# To handle StopIteration properly, use a try-except block.
print("\nHandling StopIteration with try-except:")
try:
    while True:
        print(next(iterator))
except StopIteration:
    print("Reached the end of the list.")

# 5. Built-in Functions with Iterators

# Python provides many built-in functions that work with iterators.
# Example: Using the enumerate() function to iterate with index.
print("\nUsing enumerate to iterate with index:")
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry