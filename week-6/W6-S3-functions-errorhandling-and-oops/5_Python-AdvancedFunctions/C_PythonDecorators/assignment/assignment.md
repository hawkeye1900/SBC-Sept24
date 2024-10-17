# 🐍 **Assignment: Python Decorators and Their Applications**

## 🎯 **Objective**

In this assignment, you will delve deeper into Python decorators and their applications in creating more sophisticated, reusable, and maintainable code. The focus will be on designing decorators that can handle various scenarios, such as authentication, caching, and logging, while enhancing your understanding of higher-order functions.

## 📚 **Key Learnings**

By completing this assignment, you will:

- 📦 Master decorator patterns and their practical applications.
- 🔍 Implement decorators that accept parameters and modify their behavior dynamically.
- 📊 Use decorators for complex use cases, such as caching results and managing authentication.
- 🛠️ Understand the importance of using `functools.wraps` for preserving metadata.

## 👤 **User Story**

As a developer, I want to create decorators that enhance functionality, manage complex behaviors, and maintain code readability without modifying the original functions.

## ✅ **Acceptance Criteria**

- **📝 Create a Python script named** `YOURNAME_W6S2_5_C_assignment.py`.
- The script should include:
  - **✨ Logging Decorator**: Implement a decorator that logs the execution of a function, including arguments and return values.
  - **⏱️ Timing Decorator**: Create a decorator that measures execution time and logs it, with the option to log this information to a file.
  - **📑 Parameterized Decorator**: Develop a decorator that accepts parameters, allowing the caller to specify the level of logging (INFO, DEBUG, ERROR).
  - **🔐 Authentication Decorator**: Implement a decorator that simulates user authentication for a function, requiring valid credentials to execute.
  - **💾 Caching Decorator**: Create a caching decorator that stores the results of expensive function calls to optimize performance on subsequent calls.

## 🛠️ **Steps to Complete**

1. **📁 Create a new Python file**: Name it `YOURNAME_W6S2_5_C_assignment.py`.

2. **✨ Define a Logging Decorator**:
   - Create a decorator named `logging_decorator` that logs the function name, arguments, and return value.
   - Apply this decorator to a function that performs a simple arithmetic operation (e.g., addition or multiplication).

3. **⏱️ Timing Decorator with File Logging**:
   - Develop a `timing_decorator` that measures the execution time of a function.
   - Use `functools.wraps` to preserve metadata.
   - Include an option to log execution time to a specified log file or print to the console.
   - Apply this decorator to a function that simulates a long-running process (e.g., a sorting algorithm).

4. **📑 Create a Parameterized Decorator**:
   - Implement a decorator `param_logging_decorator` that accepts a logging level parameter.
   - Use this parameter to control the verbosity of the logging output.
   - Apply this decorator to a function that processes data (e.g., filtering a list).

5. **🔐 Authentication Decorator**:
   - Create a decorator named `authentication_decorator` that requires valid credentials (e.g., username and password) to execute the wrapped function.
   - Simulate a user authentication check and deny access if the credentials are invalid.
   - Apply this decorator to a function that fetches user data.

6. **💾 Caching Decorator**:
   - Develop a caching decorator that stores the results of expensive function calls using a dictionary.
   - Check if the result for the input parameters is already cached before executing the function.
   - Apply this decorator to a function that performs a computationally expensive calculation (e.g., Fibonacci series).

## 🛠️ **Additional Challenges (Optional)**

- Extend the caching decorator to support expiration of cached results after a specified duration.
- Implement a decorator that enforces rate limiting on a function, allowing it to be called only a certain number of times within a time frame.

## 📎 **Additional Resources**

- [Python Decorators Documentation](https://docs.python.org/3/glossary.html#term-decorator)
- [Functools Module Documentation](https://docs.python.org/3/library/functools.html)
- [Decorators in Python](https://realpython.com/primer-on-python-decorators/)

Happy coding, and good luck techies!