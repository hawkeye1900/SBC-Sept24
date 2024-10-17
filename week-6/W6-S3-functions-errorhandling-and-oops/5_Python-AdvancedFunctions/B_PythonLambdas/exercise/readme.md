# 🐍 Python Lambdas

## 🎯 Challenge

Your challenge is to create a Python script that demonstrates the usage of lambda functions. Focus on defining lambda functions, using them with higher-order functions like `map()`, `filter()`, and `sorted()`.

## 📚 Key Learnings

By completing this exercise, you will learn:

- How to create and use lambda functions in Python.
- How to use lambda functions with `map()`, `filter()`, and `sorted()`.
- The advantages and limitations of using lambda functions.

## 👤 User Story

As a Python developer, I want to understand how to use lambda functions for simple, throwaway functions that are useful in functional programming contexts.

## ✅ Acceptance Criteria

- The Python script is named `lambdas.py`.
- The script demonstrates:
  - Defining and using basic lambda functions.
  - Applying lambda functions with `map()`, `filter()`, and `sorted()`.

## 🛠️ Steps to Complete

1. **📁 Create a new Python file**: Name the file `lambdas.py`.

2. **📝 Define a basic lambda function**: Create a lambda function that performs a simple operation. For example, `square = lambda x: x ** 2`.

3. **🔄 Use lambda with `map()`**: Apply the lambda function to a list of numbers using `map()`. For example, `squares = list(map(square, [1, 2, 3, 4]))`.

4. **🔍 Use lambda with `filter()`**: Filter elements of a list based on a condition using `filter()`. For example, `evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))`.

5. **🔧 Use lambda with `sorted()`**: Sort a list of tuples based on a specific element using `sorted()`. For example, `sorted_list = sorted([(1, 'apple'), (2, 'banana'), (3, 'cherry')], key=lambda x: x[1])`.

6. **📤 Print results**: Print the results of each lambda operation to verify correctness.

7. **💬 Comment your code**: Ensure that each lambda function and its usage are well-documented with comments.

## Tips

- Lambda functions are useful for short-lived operations where defining a full function might be overkill.
- Use lambda functions sparingly; they can reduce readability if overused.

## Additional Resources

- [Python Lambda Functions Documentation](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
- [Real Python: Lambda Functions](https://realpython.com/python-lambda/)
- [W3Schools: Python Lambda](https://www.w3schools.com/python/python_lambda.asp)
- [GeeksforGeeks: Python Lambda Functions](https://www.geeksforgeeks.org/python-lambda-anonymous-function/)

## Submission

Once you complete the task, submit the `lambdas.py` file to your instructor.

Happy coding tinkerers!