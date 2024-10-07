# 🐍 **Assignment: Mastering Python Error Handling and Exceptions**

## 🎯 **Objective**

In this assignment, you will deepen your understanding of error handling and exceptions in Python. You will implement various techniques for managing errors, including handling multiple exceptions, utilizing `try`, `except`, `finally`, and `else` blocks, and raising custom exceptions. This will prepare you for developing robust applications that gracefully handle unexpected situations.

## 📚 **Key Learnings**

By completing this assignment, you will:

- 🔍 Understand the importance of error handling and how to implement it effectively in Python.
- 🛠️ Utilize `try`, `except`, `finally`, and `else` blocks to manage exceptions and ensure code execution flow.
- 🔄 Handle multiple exceptions and understand when to catch specific exceptions.
- 💡 Raise and handle custom exceptions to enforce specific application constraints.
- 📊 Implement best practices for logging and debugging error messages.

## 👤 **User Story**

As a developer, I want to implement effective error handling and exception management in my Python applications to prevent unexpected crashes and ensure a smooth user experience.

## ✅ **Acceptance Criteria**

- **📝 Create a Python script named** YOURNAME_W6S3_7_A_assignment.py.
- The script should include:
  - **✨ File Handling with Error Management**: Attempt to read a file and handle any potential `FileNotFoundError`. Ensure the program continues execution regardless of the error.
  - **🔄 Multiple Exception Handling**: Create a program that accepts user input for dividing two numbers and handles both `ZeroDivisionError` and `ValueError`. 
  - **📑 Using Finally and Else Blocks**: Implement a program that connects to a database (simulated) and uses `finally` to ensure the connection closes whether an error occurs or not. 
  - **🔗 Input Validation and Custom Exception**: Validate user input to ensure a positive integer is entered. Raise a custom exception if the input is negative, and catch it to display a meaningful error message.
  - **💾 Logging Errors**: Develop a simple logging mechanism that captures errors into a text file instead of printing them to the console. Log details like the error message and timestamp.

## 🛠️ **Steps to Complete**

1. **📁 Create a new Python file**: Name it YOURNAME_W6S3_7_A_assignment.py.

2. **✨ File Handling with Error Management**:
   - Write code to attempt to open and read from a file named `data.txt`. Handle the `FileNotFoundError` to inform the user that the file does not exist, and log the error.
   - Example:
     ```python
     try:
         with open("data.txt", "r") as file:
             content = file.read()
     except FileNotFoundError:
         print("Error: The file 'data.txt' does not exist.")
         log_error("FileNotFoundError: The file 'data.txt' does not exist.")
     ```

3. **🔄 Multiple Exception Handling**:
   - Create a function that prompts the user to enter two numbers and returns their division. Handle `ZeroDivisionError` and `ValueError` to manage invalid inputs.
   - Example:
     ```python
     def divide_numbers():
         try:
             numerator = float(input("Enter the numerator: "))
             denominator = float(input("Enter the denominator: "))
             result = numerator / denominator
             print(f"The result is {result}.")
         except ZeroDivisionError:
             print("Error: Cannot divide by zero.")
             log_error("ZeroDivisionError: Cannot divide by zero.")
         except ValueError:
             print("Error: Invalid input. Please enter numeric values.")
             log_error("ValueError: Invalid input. Please enter numeric values.")
     ```

4. **📑 Using Finally and Else Blocks**:
   - Simulate a database connection and include a `finally` block to ensure that the connection closes. Use an `else` block to execute code when no exceptions occur.
   - Example:
     ```python
     def connect_to_database():
         connection = None
         try:
             # Simulating a database connection attempt
             connection = open("database.txt", "r")  # Simulating the connection
         except FileNotFoundError:
             print("Error: Database file not found.")
             log_error("FileNotFoundError: Database file not found.")
         else:
             print("Database connected successfully.")
         finally:
             if connection:
                 connection.close()
                 print("Database connection closed.")
     ```

5. **🔗 Input Validation and Custom Exception**:
   - Write a program to validate user input for a positive integer. Raise a `ValueError` if the input is negative and catch it to display an appropriate message.
   - Example:
     ```python
     def check_positive_integer():
         try:
             user_input = int(input("Enter a positive integer: "))
             if user_input < 0:
                 raise ValueError("Input cannot be negative.")
         except ValueError as e:
             print(f"Error: {e}")
             log_error(f"ValueError: {e}")
     ```

6. **💾 Logging Errors**:
   - Implement a simple logging function that writes error messages to a file named `error_log.txt` along with the timestamp.
   - Example:
     ```python
     from datetime import datetime

     def log_error(message):
         with open("error_log.txt", "a") as log_file:
             log_file.write(f"{datetime.now()}: {message}\n")
     ```

## 🛠️ **Additional Challenges (Optional)**

- **🌀 Advanced Logging**: Extend the logging function to capture more details, such as the line number where the error occurred or the type of exception.
- **⏳ Timeout Management**: Simulate a network request with a timeout. Implement exception handling for cases where the request exceeds a specified duration.

## 📎 **Additional Resources**

- [Python Exception Handling Documentation](https://docs.python.org/3/tutorial/errors.html)
- [Real Python: Python Exception Handling](https://realpython.com/python-exceptions/)
- [W3Schools Python Try Except](https://www.w3schools.com/python/python_try_except.asp)

Happy coding, and good luck techies!