# 🐍 Python Error Handling and Exceptions

## 🎯 Challenge

Your challenge is to create a Python script that demonstrates how to handle exceptions using `try`, `except`, `finally`, and how to raise custom exceptions when necessary.

## 📚 Key Learnings

By completing this exercise, you will learn:

- How to use `try`, `except`, and `finally` blocks to handle exceptions in Python.
- How to raise custom exceptions with meaningful messages.
- The importance of exception handling for making code robust and error-resistant.

## 👤 User Story

As a Python developer, I want to handle potential errors in my code gracefully to avoid unexpected crashes and ensure a smooth user experience.

## ✅ Acceptance Criteria

- The Python script is named `error_handling.py`.
- The script demonstrates:
  - Catching exceptions using `try` and `except` blocks.
  - Raising custom exceptions using `raise`.
  - Using `finally` to execute code regardless of exceptions.

## 🛠️ Steps to Complete

1. **📁 Create a new Python file**: Name the file `error_handling.py`.

2. **🔧 Set up a `try` and `except` block**: Write code that catches common exceptions like `ZeroDivisionError` or `ValueError`. For example:
    ```python
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("You cannot divide by zero!")
    ```

3. **🔍 Handle multiple exceptions**: Show how to handle different types of exceptions in a single `try` block. For example:
    ```python
    try:
        number = int("invalid")
    except (ValueError, TypeError) as e:
        print(f"An error occurred: {e}")
    ```

4. **🌟 Use `finally`**: Ensure that some code runs regardless of whether an exception occurred. For example:
    ```python
    try:
        file = open("test.txt", "r")
    finally:
        print("This will run no matter what.")
    ```

5. **✋ Raise a custom exception**: Demonstrate how to raise a custom exception with a meaningful message. For example:
    ```python
    if age < 0:
        raise ValueError("Age cannot be negative!")
    ```

6. **📤 Print results**: Output the results to demonstrate exception handling in action.

7. **💬 Comment your code**: Ensure that each section of the script is properly commented for clarity.

## Tips

- Exception handling is essential for creating robust applications.
- Avoid using broad `except` statements, and be specific about the exceptions you handle.

## Additional Resources

- [Python Error Handling Documentation](https://docs.python.org/3/tutorial/errors.html)
- [Real Python: Exception Handling in Python](https://realpython.com/python-exceptions/)
- [GeeksforGeeks: Python Error Handling](https://www.geeksforgeeks.org/python-exception-handling/)
- [W3Schools: Python Try Except](https://www.w3schools.com/python/python_try_except.asp)

## Submission

Once you complete the task, submit the `error_handling.py` file to your instructor.

Happy coding technocrats!