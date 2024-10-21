# 🐍 **Assignment: Python Generators for Efficient Data Handling**

## 🎯 **Objective**

In this assignment, you will dive deep into Python generators, a powerful tool for handling large datasets efficiently. The focus will be on implementing custom generators that handle large sequences without consuming excessive memory, and building complex use cases such as data streaming and processing pipelines.

## 📚 **Key Learnings**

By completing this assignment, you will:

- 🛠️ Master Python generator functions and their practical applications.
- 🔍 Understand how to use `yield` and `next()` to build custom generators.
- 🚀 Create efficient code that handles large datasets without high memory consumption.
- 📊 Implement generators for data streaming, filtering, and processing in real-time.

## 👤 **User Story**

As a developer, I want to implement generators that allow efficient iteration over large datasets, providing flexibility for real-time data processing and memory efficiency.

## ✅ **Acceptance Criteria**

- **📝 Create a Python script named** `YOURNAME_W6S2_5_D_assignment.py`.
- The script should include:
  - **✨ Basic Generator Function**: Implement a generator function that yields numbers in a specified range with a custom step.
  - **🔄 Fibonacci Generator**: Create a generator that produces Fibonacci numbers up to a maximum value.
  - **📑 Generator with Filtering**: Implement a generator that filters a large dataset based on a specific condition (e.g., yields only even numbers).
  - **🔗 Chained Generators**: Build two generators and chain them to create a processing pipeline.
  - **💾 Data Streaming Example**: Create a generator that simulates streaming data (e.g., reading from a file or an API).
  
## 🛠️ **Steps to Complete**

1. **📁 Create a new Python file**: Name it `YOURNAME_W6S2_5_D_assignment.py`.

2. **✨ Basic Generator Function**:
   - Define a generator function `range_with_step(start, stop, step)` that yields numbers from `start` to `stop` with the specified `step`.
   - Example usage: 
     ```python
     for num in range_with_step(0, 10, 2):
         print(num)
     # Output: 0, 2, 4, 6, 8
     ```

3. **🔄 Fibonacci Generator**:
   - Implement a generator `fibonacci_gen(max_val)` that yields Fibonacci numbers up to a given maximum value (`max_val`).
   - Example usage:
     ```python
     for fib in fibonacci_gen(100):
         print(fib)
     # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
     ```

4. **📑 Generator with Filtering**:
   - Create a generator `filter_even_numbers(data)` that filters even numbers from a given dataset.
   - Apply this generator to a large list of numbers to yield only even numbers.
   - Example usage:
     ```python
     data = range(1, 101)
     for even_num in filter_even_numbers(data):
         print(even_num)
     # Output: 2, 4, 6, ..., 100
     ```

5. **🔗 Chained Generators**:
   - Build two generators: one that produces a sequence of numbers, and another that squares those numbers. Chain them together to create a processing pipeline.
   - Example:
     ```python
     def number_gen():
         yield from range(1, 10)

     def square_gen(nums):
         for num in nums:
             yield num ** 2

     for squared in square_gen(number_gen()):
         print(squared)
     # Output: 1, 4, 9, 16, ..., 81
     ```

6. **💾 Data Streaming Example**:
   - Implement a generator `data_stream(file_path)` that reads data from a large file or simulates streaming data from an API.
   - Use `yield` to return one line or chunk of data at a time.
   - Example usage:
     ```python
     def data_stream(file_path):
         with open(file_path, 'r') as file:
             for line in file:
                 yield line.strip()

     for line in data_stream('large_file.txt'):
         print(line)
     # Output: Prints each line of the file one by one.
     ```

## 🛠️ **Additional Challenges (Optional)**

- **🌀 Infinite Generator**: Create a generator that generates an infinite sequence of prime numbers.
- **⏳ Time-Based Streaming**: Extend the data streaming generator to simulate real-time data streams, where new data is available at specific time intervals (e.g., every 2 seconds).

## 📎 **Additional Resources**

- [Python Generators Documentation](https://docs.python.org/3/tutorial/classes.html#generators)
- [Real Python Generators Tutorial](https://realpython.com/introduction-to-python-generators/)
- [Efficient Data Processing with Generators](https://docs.python.org/3/howto/functional.html#generators)

Happy coding, and good luck techies!