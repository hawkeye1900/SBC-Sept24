
# 🐍 Python Functions and Lambdas

## 🎯 Challenge

Your challenge is to create two Python scripts: one that demonstrates the usage of functions and another that showcases lambda functions. Focus on defining functions, passing arguments, returning values, and using lambda functions with higher-order functions like `map()`, `filter()`, and `sorted()`.

## 📚 Key Learnings

By completing this exercise, you will learn:

- How to define and call functions in Python.
- How to use parameters and return values in functions.
- How to handle default arguments and variable-length arguments.
- How to create and use lambda functions in Python.
- How to apply lambda functions with `map()`, `filter()`, and `sorted()`.

## 👤 User Story

As a Python developer, I want to understand how to effectively define and use functions and lambda functions to organize code, reuse logic, and simplify complex tasks.

## ✅ Acceptance Criteria

1. **Python Script for Functions**: The script is named `functions.py` and demonstrates:
   - Defining functions with and without parameters.
   - Using default arguments and keyword arguments.
   - Returning values from functions.
   - Using variable-length arguments (`*args` and `**kwargs`).
  
2. **Python Script for Lambdas**: The script is named `lambdas.py` and demonstrates:
   - Defining and using basic lambda functions.
   - Applying lambda functions with `map()`, `filter()`, and `sorted()`.

## 🛠️ Steps to Complete

### For `functions.py`

1. **📁 Create a new Python file**: Name the file `functions.py`.

2. **📝 Define a basic function**: Create a function that takes no parameters and returns a value. 
   ```python
   def greet():
       return "Hello, World!"
   ```

3. **🔧 Add parameters**: Define a function that takes parameters and returns a result. 
   ```python
   def add(a, b):
       return a + b
   ```

4. **🌟 Use default arguments**: Create a function with default arguments. 
   ```python
   def greet(name="Guest"):
       return f"Hello, {name}!"
   ```

5. **📦 Handle variable-length arguments**: Define a function that accepts a variable number of arguments using `*args` and `**kwargs`. 
   ```python
   def print_info(*args, **kwargs):
       print("Positional arguments:", args)
       print("Keyword arguments:", kwargs)
   ```

6. **📤 Print results**: Test your functions by calling them and printing the results.

7. **💬 Comment your code**: Ensure that each function is well-documented with comments explaining its purpose and usage.

### For `lambdas.py`

1. **📁 Create a new Python file**: Name the file `lambdas.py`.

2. **📝 Define a basic lambda function**: Create a lambda function that performs a simple operation. 
   ```python
   square = lambda x: x ** 2
   ```

3. **🔄 Use lambda with `map()`**: Apply the lambda function to a list of numbers using `map()`. 
   ```python
   squares = list(map(square, [1, 2, 3, 4]))
   ```

4. **🔍 Use lambda with `filter()`**: Filter elements of a list based on a condition using `filter()`. 
   ```python
   evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
   ```

5. **🔧 Use lambda with `sorted()`**: Sort a list of tuples based on a specific element using `sorted()`. 
   ```python
   sorted_list = sorted([(1, 'apple'), (2, 'banana'), (3, 'cherry')], key=lambda x: x[1])
   ```

6. **📤 Print results**: Print the results of each lambda operation to verify correctness.

7. **💬 Comment your code**: Ensure that each lambda function and its usage are well-documented with comments.

## Tips

- Functions help in breaking down complex problems into smaller, manageable tasks.
- Lambda functions are useful for short-lived operations where defining a full function might be overkill.
- Use docstrings and comments for better readability and maintainability.

## Additional Resources

- [Python Functions Documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Real Python: Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)
- [Python Lambda Functions Documentation](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
- [Real Python: Lambda Functions](https://realpython.com/python-lambda/)

## Submission

Once you complete the tasks, submit both `functions.py` and `lambdas.py` files to your instructor.

Happy coding, architects and tinkerers!
