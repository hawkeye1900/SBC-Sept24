# 🐍 **Assignment: Python Functions with Advanced Operations**

## 🎯 **Objective**

Your task is to write a Python program that demonstrates the use of functions in combination with strings, dictionaries, and regular expressions. This assignment will challenge you to create reusable functions that incorporate string manipulations, user data handling, and validation using regular expressions.

## 📚 **Key Learnings**

By completing this assignment, you will:

- 📦 Deepen your understanding of Python functions, including default arguments, parameterized functions, and return values.
- 🔍 Apply regular expressions within functions for validating input and extracting specific patterns from text.
- 📚 Utilize dictionaries to manage and process user data.
- 🔄 Practice advanced string manipulations within functions.

## 👤 **User Story**

As a developer, I want to create efficient and reusable functions to process strings, validate user data using regular expressions, and manage information in dictionaries.

## ✅ **Acceptance Criteria**

- **📝 Create a Python script named** `YOURNAME_W6S2_5_A_assignment.py`.
- The script should demonstrate the following:
  - **✨ Basic Function**: A simple function that returns a greeting message.
  - **🧮 Function with Parameters**: A function that accepts two strings (name and age), combines them, and returns a formatted message.
  - **🛠️ Default Arguments**: A function that returns a greeting message with a default name.
  - **🔍 Regular Expression Function**: A function that validates if a user-provided phone number follows a specific format (e.g., `(123) 456-7890`).
  - **📚 Dictionary Handling**: A function that accepts user details (name, email, and phone number) in a dictionary and processes the data:
    - Validates the email format using a regular expression.
    - Prints a success message if both the email and phone number are valid.
  - **🔄 Return Multiple Values**: A function that returns both valid and invalid entries from a dictionary of user data.
  - **📜 Use of String Methods**: A function that demonstrates advanced string methods (e.g., `replace()`, `upper()`, and `strip()`) within the above functions.

## 🛠️ **Steps to Complete**

1. **📁 Create a new Python file**: Name it `YOURNAME_W6S2_5_A_assignment.py`.
2. **📝 Define a Basic Function**:
   - Create a simple function `greet()` that returns a greeting message like "Hello, World!".
3. **🧮 Define a Function with Parameters**:
   - Create a function `create_message(name, age)` that takes a name and age as strings, then returns a message like `"Name: Alice, Age: 25"`.
4. **🛠️ Define a Function with Default Arguments**:
   - Create a function `greet(name="Guest")` that returns a personalized greeting message using the given `name`. If no name is provided, it should default to "Guest".
5. **🔍 Function with Regular Expressions**:
   - Create a function `validate_phone(phone)` that checks if the phone number follows the format `(XXX) XXX-XXXX`.
   - Example pattern for phone numbers: `r'\(\d{3}\) \d{3}-\d{4}'`.
   - Return `True` if valid, otherwise return `False`.
6. **📚 Function Handling a Dictionary**:
   - Create a function `process_user_info(user_data)` that accepts a dictionary with keys `'name'`, `'email'`, and `'phone'`.
   - Validate the email format using a regular expression (`r'^\w+@\w+\.\w{2,3}$'`).
   - Validate the phone number using the `validate_phone()` function.
   - If both are valid, return a success message like `"User info is valid"`.
   - If not, return an error message.
7. **🔄 Function Returning Multiple Values**:
   - Create a function `check_users(user_dict)` that accepts a dictionary where each key is a user’s name and each value is another dictionary with user details (e.g., email and phone).
   - The function should return two dictionaries: one for users with valid data and one for invalid data.
8. **📜 String Method Manipulation**:
   - Within the functions, apply string methods (like `replace()`, `upper()`, `strip()`) to manipulate the input data before validation.
   - For example, ensure phone numbers are stripped of any leading/trailing whitespace.

## 📎 **Additional Resources**

- [Python Functions Documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Regular Expressions Documentation](https://docs.python.org/3/library/re.html)
- [Python Dictionaries Documentation](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python String Methods Documentation](https://www.w3schools.com/python/python_ref_string.asp)

Happy coding, and good luck guys!