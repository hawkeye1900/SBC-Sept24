# ----------------------------
# Python Functions and Lambdas
# ----------------------------

# Python Functions
# Functions are essential for modular programming, allowing code to be reused and organized.

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

# ----------------------------
# Python Lambdas
# ----------------------------

# Lambda functions are small, anonymous functions defined with the `lambda` keyword.
# They can have any number of arguments but only one expression.

# Basic Lambda Function
square = lambda x: x ** 2
print("Square of 5:", square(5))  # Output: Square of 5: 25

# Lambda with map()
# Applying the lambda function to a list of numbers to get their squares
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print("Squares of numbers:", squares)  # Output: Squares of numbers: [1, 4, 9, 16]

# Lambda with filter()
# Filtering out even numbers from a list
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)  # Output: Even numbers: [2, 4]

# Lambda with sorted()
# Sorting a list of tuples by the second element
tuple_list = [(4, 'pineapple'), (2, 'banana'), (3, 'cherry')]
sorted_list = sorted(tuple_list, key=lambda x: x[1])
print("Sorted list by second element:", sorted_list)  # Output: Sorted list by second element: [(2, 'banana'), (3, 'cherry'), (4, 'pineapple')]

# Summary
# Functions help organize code into reusable blocks, improving structure and readability.
# Lambda functions are useful for simple operations and can be combined with functions like map(), filter(), and sorted().
# While powerful, they should be used judiciously to maintain code readability.