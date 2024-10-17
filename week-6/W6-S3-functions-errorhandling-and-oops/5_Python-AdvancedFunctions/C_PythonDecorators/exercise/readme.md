# 🐍 Python Decorators

## 🎯 Challenge

Your challenge is to create a Python script that demonstrates the usage of decorators. Focus on defining basic decorators, applying them to functions, and understanding their use cases.

## 📚 Key Learnings

By completing this exercise, you will learn:

- How to define and use decorators in Python.
- How decorators can modify or extend the behavior of functions.
- The concept of higher-order functions and function wrappers.

## 👤 User Story

As a Python developer, I want to understand how to use decorators to add functionality to existing functions in a clean and reusable way.

## ✅ Acceptance Criteria

- The Python script is named `decorators.py`.
- The script demonstrates:
  - Defining a simple decorator.
  - Applying the decorator to a function.
  - Using decorators with parameters.

## 🛠️ Steps to Complete

1. **📁 Create a new Python file**: Name the file `decorators.py`.

2. **📝 Define a basic decorator**: Create a decorator function that prints a message before and after the execution of a function. For example:
    ```python
    def simple_decorator(func):
        def wrapper():
            print("Before function call")
            func()
            print("After function call")
        return wrapper
    ```

3. **🔄 Apply the decorator**: Use the `@decorator_name` syntax to apply the decorator to a function. For example:
    ```python
    @simple_decorator
    def greet():
        print("Hello!")
    ```

4. **📤 Print results**: Call the decorated function and observe the output.

5. **✏️ Use decorators with parameters**: Modify the decorator to accept parameters and use it to log the execution time of a function.

6. **💬 Comment your code**: Ensure that each decorator and its usage are well-documented with comments.

## Tips

- Decorators are a powerful feature for modifying or extending function behavior without modifying the function itself.
- Use `functools.wraps` in decorators to preserve the metadata of the original function.

## Additional Resources

- [Python Decorators Documentation](https://docs.python.org/3/glossary.html#term-decorator)
- [Real Python: Python Decorators](https://realpython.com/primer-on-python-decorators/)
- [W3Schools: Python Decorators](https://www.w3schools.com/python/python_decorators.asp)
- [GeeksforGeeks: Python Decorators](https://www.geeksforgeeks.org/decorators-in-python/)

## Submission

Once you complete the task, submit the `decorators.py` file to your instructor.

Happy coding cyberpunks!