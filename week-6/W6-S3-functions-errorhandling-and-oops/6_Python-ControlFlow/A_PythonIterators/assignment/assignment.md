# 🐍 **Assignment: Advanced Python Iterators**

## 🎯 **Objective**

In this assignment, you will explore advanced concepts of Python iterators, focusing on creating custom iterators, handling the `StopIteration` exception, and working with built-in Python functions like `enumerate()` and `zip()` with iterators. You will also chain iterators to create more complex workflows.

## 📚 **Key Learnings**

By completing this assignment, you will:

- 🛠️ Gain in-depth knowledge of how Python iterators work under the hood.
- 🔍 Master the usage of `iter()`, `next()`, and custom iterator classes.
- 🚀 Implement iterators with built-in functions to enhance productivity.
- 📑 Handle `StopIteration` errors gracefully using proper exception handling.
- 🔗 Chain iterators and create iterable processing pipelines.

## 👤 **User Story**

As an experienced developer, I want to create advanced iterator solutions for processing data from lists, strings, and other iterable objects, while ensuring performance and error handling.

## ✅ **Acceptance Criteria**

- **📝 Create a Python script named** `YOURNAME_W6S3_6_A_assignment.py`.
- The script should include:
  - **✨ Custom Iterator Class**: Implement a custom iterator class that simulates the behavior of Python’s `iter()` and `next()` with a sequence of your choice.
  - **🔄 Complex String Iterator**: Implement an iterator for a string that yields each character in uppercase until it reaches a stopping character.
  - **📑 StopIteration Handling**: Use a `try-except` block to handle `StopIteration` exceptions while iterating through a list.
  - **📊 Built-in Functions with Iterators**: Use `enumerate()` and `zip()` to iterate over multiple iterables simultaneously, generating index-value pairs and zipped tuples.
  - **🔗 Chained Iterators**: Chain two or more iterators to process data in multiple stages, applying transformations between them.

## 🛠️ **Steps to Complete**

1. **📁 Create a new Python file**: Name it `YOURNAME_W6S3_6_A_assignment.py`.

2. **✨ Custom Iterator Class**:
   - Define a class `CustomIterator` that takes a list as input and implements the `__iter__()` and `__next__()` methods.
   - The iterator should return elements in reverse order, and raise `StopIteration` when all elements have been iterated.
   

3. **🔄 Complex String Iterator**:
   - Create an iterator for a string that yields each character in uppercase until it reaches a specific stopping character (e.g., `!`).
   - If the stopping character is reached, raise `StopIteration`.

4. **📑 StopIteration Handling**:
   - Create an iterator for a list of numbers and handle `StopIteration` using a `try-except` block.

5. **📊 Built-in Functions with Iterators**:
   - Use `enumerate()` to iterate over a list of fruits with both index and item.
   - Combine `zip()` with multiple iterables (e.g., two lists) to iterate over them simultaneously.

6. **🔗 Chained Iterators**:
   - Create two iterators: one that generates a sequence of numbers, and another that filters out even numbers from the sequence.
   - Chain these iterators to create a processing pipeline.

## 🛠️ **Additional Challenges (Optional)**

- **🌀 Infinite Custom Iterator**: Create a custom iterator class that generates an infinite sequence of natural numbers. Implement proper safeguards to avoid infinite loops during iteration.
- **🔄 Complex Chaining**: Extend the chained iterators to apply multiple transformations, such as filtering odd numbers and squaring the result in multiple stages.

## 📎 **Additional Resources**

- [Python Iterators Documentation](https://docs.python.org/3/tutorial/classes.html#iterators)
- [Real Python Iterator Tutorial](https://realpython.com/python-itertools/)
- [Advanced Iterators in Python](https://towardsdatascience.com/how-to-use-python-itertools-for-data-science-and-machine-learning-6b9dd8c44b9b)

Happy coding, and good luck techies!