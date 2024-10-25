# ----------------------------
# Python Decorators and Generators
# ----------------------------

# Decorators are a way to modify or extend the behavior of functions or methods.
# They are higher-order functions that take another function as an argument and return a new function that adds some kind of functionality.

# Basic Decorator Example
def simple_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

# Applying the decorator
@simple_decorator
def greet():
    print("Hello!")

# Calling the decorated function
greet()
# Output:
# Before function call
# Hello!
# After function call

# Decorator with Parameters Example
from functools import wraps
import time

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@timing_decorator
def long_running_task():
    time.sleep(2)  # Simulates a long-running task
    print("Task complete")

# Calling the function with the timing decorator
long_running_task()
# Output(expected):
# Execution time: 2.002345 seconds
# Task complete

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
print("\nCounting up to 5:")
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

# Decorators and generators are powerful features in Python that allow for cleaner, more efficient, and reusable code.