# ----------------------------
# Python Functions
# ----------------------------

# Basic Function
def greet():
    """
    A simple function that returns a greeting message.
    """
    return "Hello, World!"

print("Greeting:", greet())  # Output: Greeting: Hello, World!

# Function with Parameters
def add(a, b):
    """
    Adds two numbers and returns the result.
    :param a: First number
    :param b: Second number
    :return: Sum of a and b
    """
    return a + b

print("Sum of 5 and 3:", add(5, 3))  # Output: Sum of 5 and 3: 8

# Function with Default Arguments
def greet(name="Guest"):
    """
    Returns a personalized greeting message.
    :param name: Name of the person to greet (default is 'Guest')
    :return: Greeting message
    """
    return f"Hello, {name}!"

print(greet())  # Output: Hello, Guest!
print(greet("Alice"))  # Output: Hello, Alice!

# Function with Variable-Length Arguments
def print_info(*args, **kwargs):
    """
    Prints variable-length positional and keyword arguments.
    :param args: Positional arguments
    :param kwargs: Keyword arguments
    """
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_info(1, 2, 3, name="Alice", age=25)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 25}


# Functions are essential for modular programming, allowing code to be reused and organized.
# Understanding how to define and use functions will improve the structure and readability of your code.