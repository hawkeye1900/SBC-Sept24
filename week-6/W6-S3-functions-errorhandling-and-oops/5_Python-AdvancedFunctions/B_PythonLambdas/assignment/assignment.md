# 🐍 **Assignment: Python Functions with Lambda Operations and Advanced Use Cases**

## 🎯 **Objective**

In this assignment, you will deepen your understanding of Python functions, including lambdas, variable-length arguments, and regular expressions. The task focuses on creating reusable, efficient code that handles data validation and processing using functions and lambda expressions.

## 📚 **Key Learnings**

By completing this assignment, you will:

- 📦 Master Python functions, lambdas, and argument handling.
- 🔍 Use regular expressions for validating and extracting patterns from text.
- 📚 Manipulate data using lambda functions within map(), filter(), and sorted().
- 📊 Enhance the use of dictionaries to process and validate complex user data.

## 👤 **User Story**

As a developer, I want to implement modular, reusable functions that utilize lambdas for short operations, manage dictionaries, and validate user input using regular expressions.

## ✅ **Acceptance Criteria**

- **📝 Create a Python script named** `YOURNAME_W6S2_5_B_assignment.py`.
- The script should include:
  - **✨ Basic Lambda Function**: A lambda function that squares a number.
  - **🧮 Lambda with Parameters**: Use lambdas with `map()` to perform calculations on a list of numbers.
  - **📑 Lambda for String Filtering**: Use a lambda with `filter()` to extract strings from a list that match a specific pattern.
  - **📚 Lambda with Sorting**: Use a lambda function to sort a list of tuples by a chosen element.
  - **🔍 Function with Regular Expressions**: A function that validates email format using regular expressions.
  - **📚 Dictionary Handling with Lambdas**: A function that processes user data using dictionaries and lambda functions for quick operations.
  - **🔄 Function Returning Multiple Values**: A function that returns valid and invalid users based on data validation.

## 🛠️ **Steps to Complete**

1. **📁 Create a new Python file**: Name it `YOURNAME_W6S2_5_B_assignment.py`.

2. **✨ Define a Basic Lambda Function**:
   - Create a lambda function `square` that takes an integer and returns its square.
   - Example: `square = lambda x: x ** 2`.

3. **🧮 Lambda with Parameters**:
   - Use a lambda with `map()` to apply the square function to a list of numbers `[1, 2, 3, 4]`.
   - Return the list of squared values.

4. **📑 Lambda for String Filtering**:
   - Create a list of strings `["apple", "banana", "cherry", "pineapple"]`.
   - Use a lambda with `filter()` to extract strings that contain the letter "a".
   - Print the filtered result.

5. **📚 Lambda with Sorting**:
   - Given a list of tuples: `[(1, 'apple'), (3, 'cherry'), (2, 'banana')]`.
   - Use `sorted()` with a lambda function to sort the list by the second element (the fruit name).
   - Return the sorted list.

6. **🔍 Function with Regular Expressions**:
   - Create a function `validate_email(email)` that checks if an email is valid using the regular expression `r'^\w+@\w+\.\w{2,3}$'`.
   - Return `True` if valid, otherwise `False`.

7. **📚 Dictionary Handling with Lambdas**:
   - Create a function `process_user_info(user_data)` that accepts a dictionary with user data (`'name'`, `'email'`, `'phone'`).
   - Use lambdas to:
     - Validate email format.
     - Extract only numbers from the phone number using `filter()` and a lambda function.
     - If both email and phone are valid, return a success message.
     - If invalid, return an error message.

## 🛠️ **Additional Challenges (Optional)**

- Modify the dictionary handling function to accept additional user data (e.g., age) and validate it.
- Use a lambda with `sorted()` to sort users by age in ascending order.

## 📎 **Additional Resources**

- [Python Functions Documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Regular Expressions Documentation](https://docs.python.org/3/library/re.html)
- [Python Lambda Functions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)

Happy coding, and good luck techies!