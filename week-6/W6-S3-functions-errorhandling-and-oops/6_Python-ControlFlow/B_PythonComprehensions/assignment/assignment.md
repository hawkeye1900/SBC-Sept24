# 🐍 **Assignment: Python Comprehensions for Data Manipulation**

## 🎯 **Objective**

In this assignment, you will explore the powerful Python comprehension techniques for working with collections like lists, sets, and dictionaries. The focus will be on leveraging comprehensions for data transformation, filtering, and mapping. You will implement real-world scenarios that go beyond basic usage, pushing your understanding of Python comprehensions to the next level.

## 📚 **Key Learnings**

By completing this assignment, you will:

- 💡 Master list, set, and dictionary comprehensions for transforming and filtering data in one-liners.
- 🔍 Understand how to incorporate conditional logic into comprehensions for data selection.
- 🚀 Learn how to use nested comprehensions for complex data structures.
- 📊 Apply comprehensions in practical data manipulation tasks like flattening nested lists and processing complex dictionaries.

## 👤 **User Story**

As a developer, I want to implement Python comprehensions that allow for efficient transformation and filtering of data, providing clean, readable, and powerful one-liner code.

## ✅ **Acceptance Criteria**

- **📝 Create a Python script named** YOURNAME_W6S3_6_B_assignment.py.
- The script should include:
  - **✨ Advanced List Comprehension**: Generate a list of numbers and apply both transformation and filtering in a single comprehension.
  - **🔄 Nested List Comprehension**: Use comprehensions to flatten a nested list structure.
  - **📑 Set Comprehension with Conditions**: Create a set comprehension that filters and transforms data.
  - **🔗 Complex Dictionary Comprehension**: Build a dictionary using a comprehension with conditional logic for filtering and mapping.
  - **💡 Real-World Scenario**: Apply comprehensions in a real-world data manipulation task (e.g., processing log data or transforming a CSV file).

## 🛠️ **Steps to Complete**

1. **📁 Create a new Python file**: Name it YOURNAME_W6S3_6_B_assignment.py.

2. **✨ Advanced List Comprehension**:
   - Create a list comprehension that generates a list of squares of all odd numbers between 1 and 20.
   - Incorporate both transformation (squaring the numbers) and filtering (selecting only odd numbers) into a single comprehension.
   
3. **🔄 Nested List Comprehension**:
   - Use a nested list comprehension to flatten a 2D list (a list of lists) into a 1D list.
  
4. **📑 Set Comprehension with Conditions**:
   - Create a set comprehension that generates the set of unique even numbers between 1 and 20, but only includes numbers greater than 10.
  
5. **🔗 Complex Dictionary Comprehension**:
   - Build a dictionary comprehension that maps numbers from 1 to 10 to their cubes, but only include numbers that are divisible by 3.

6. **💡 Real-World Scenario: Log Data Processing**:
   - Simulate processing log data. Given a list of log entries (represented as strings), use a list comprehension to extract only the log entries that contain the word "ERROR" and convert them to uppercase.
   - Example logs = [
         "INFO: User login successful",
         "ERROR: Unable to connect to the server",
         "WARNING: Low disk space",
         "ERROR: File not found"
     ]
    

## 🛠️ **Additional Challenges (Optional)**

- **🌀 Nested Dictionary Comprehension**: Create a dictionary comprehension that processes a dictionary of dictionaries. For instance, you can filter and transform key-value pairs in a nested dictionary where the values are themselves dictionaries.
- **⏳ Performance Benchmark**: Compare the performance of comprehensions with traditional for-loops using the `timeit` module for a large dataset.

## 📎 **Additional Resources**

- [Python Comprehensions Documentation](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Real Python: Comprehensions](https://realpython.com/list-comprehension-python/)
- [Pythonic Data Transformation with Comprehensions](https://docs.python.org/3/howto/functional.html#data-structures)

Happy coding, and enjoy the power of comprehensions! 🚀