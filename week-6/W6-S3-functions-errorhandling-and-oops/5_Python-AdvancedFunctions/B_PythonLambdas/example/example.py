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
print("Sorted list by second element:", sorted_list)  # Output: Sorted list by second element: [(1, 'apple'), (2, 'banana'), (3, 'cherry')]

# Lambda functions are useful for simple, short-term operations and can be used with functions like map(), filter(), and sorted().
# While powerful, they should be used judiciously to maintain code readability.