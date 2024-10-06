# ----------------------------
# Python Decorators
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

# Decorators provide a way to add or modify functionality in a clean, reusable manner.
# They are particularly useful for logging, timing, and access control tasks.