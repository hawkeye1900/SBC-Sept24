# 🐍 **Assignment: Mastering Python Loops**

## 🎯 **Objective**

In this assignment, you will deepen your understanding of loops in Python. You will implement various types of loops, explore control flow statements like `break` and `continue`, and create more complex iterations to solve practical problems. This will prepare you for real-world applications where repetitive tasks and data manipulation are crucial.

## 📚 **Key Learnings**

By completing this assignment, you will:

- 🛠️ Master `for` and `while` loops for iterating over different data structures.
- 🔄 Understand the use of control flow statements (`break` and `continue`) to manage loop execution.
- 📊 Implement nested loops to solve more complex problems, such as multi-dimensional data processing.
- 💡 Utilize loops in combination with conditional statements to create dynamic solutions.

## 👤 **User Story**

As a developer, I want to effectively utilize loops and control flow in Python to process data and automate repetitive tasks, allowing for efficient code execution and increased productivity.

## ✅ **Acceptance Criteria**

- **📝 Create a Python script named** YOURNAME_W6S3_6_C_assignment.py.
- The script should include:
  - **✨ List Manipulation with Loops**: Iterate over a list of dictionaries (e.g., representing a collection of students) and print details about each student, such as their names and grades.
  - **🔄 Nested Loops**: Implement a nested loop to create a multiplication table (up to 10) and print it in a formatted manner.
  - **📑 Break and Continue Statements**: Create a program that counts the number of valid input entries from the user, where invalid inputs (like strings) are ignored, using `continue` and `break` appropriately.
  - **🔗 Looping Through a Dictionary**: Use a `for` loop to iterate over a dictionary representing stock prices of various companies and print those above a specified threshold.
  - **💾 Data Filtering with Loops**: Develop a program that filters out and displays only the odd numbers from a list of numbers, demonstrating the use of the `continue` statement.

## 🛠️ **Steps to Complete**

1. **📁 Create a new Python file**: Name it YOURNAME_W6S3_6_C_assignment.py.

2. **✨ List Manipulation with Loops**:
   - Create a list of dictionaries representing students, where each dictionary contains a student's name and grade.
   - Use a `for` loop to iterate through the list and print each student's name and their grade.
   - Example structure:
     ```python
     students = [
         {"name": "Alice", "grade": 85},
         {"name": "Bob", "grade": 90},
         {"name": "Charlie", "grade": 78}
     ]
     ```

3. **🔄 Nested Loops**:
   - Implement a nested loop to generate a multiplication table for numbers from 1 to 10.
   - Format the output so that it resembles a traditional table.
   - Example:
     ```python
     for i in range(1, 11):
         for j in range(1, 11):
             print(f"{i * j:3}", end=" ")
         print()
     ```

4. **📑 Break and Continue Statements**:
   - Create a program that prompts the user to enter numbers until they enter a non-numeric value. Use `continue` to skip non-numeric entries and `break` to exit when the user types 'exit'.
   - Maintain a count of valid entries and display the total count at the end.

5. **🔗 Looping Through a Dictionary**:
   - Create a dictionary representing stock prices (e.g., `{"AAPL": 150, "GOOGL": 2800, "TSLA": 700}`).
   - Use a `for` loop to iterate through the dictionary and print out companies with stock prices above a specified threshold (e.g., 1000).

6. **💾 Data Filtering with Loops**:
   - Create a list of integers ranging from 1 to 50.
   - Use a loop to filter out and print only the odd numbers from the list.
   - Make sure to use the `continue` statement to skip even numbers.

## 🛠️ **Additional Challenges (Optional)**

- **🌀 Advanced Input Validation**: Extend the user input validation program to count the number of even and odd numbers separately, providing a summary at the end.
- **⏳ Time-Based Filtering**: Create a program that generates random stock prices every few seconds and prints only the prices that exceed a threshold until a specified time limit.

## 📎 **Additional Resources**

- [Python Loops Documentation](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [W3Schools Python Loops Tutorial](https://www.w3schools.com/python/python_for_loops.asp)
- [Real Python: Python Loops](https://realpython.com/python-for-loop/)

Happy coding, and good luck techies!