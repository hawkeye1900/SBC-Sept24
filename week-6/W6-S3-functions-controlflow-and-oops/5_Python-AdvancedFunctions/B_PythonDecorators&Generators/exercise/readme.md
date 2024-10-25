# 🐍 Python Decorators and Generators

## 🎯 Challenge

Your challenge is to create two Python scripts that demonstrate the usage of decorators and generators. Focus on defining basic decorators and generators, applying them, and understanding their use cases and advantages.

## 📚 Key Learnings

By completing these exercises, you will learn:

- How to define and use decorators and generators in Python.
- How decorators can modify or extend the behavior of functions.
- The concept of higher-order functions and function wrappers.
- The difference between generators and regular functions.
- How generators can iterate over large sequences efficiently.

## 👤 User Story

As a Python developer, I want to understand how to use decorators to add functionality to existing functions and how to use generators to create iterators that produce items on-the-fly, especially when working with large datasets.

---

## Exercise 1: Python Decorators

### ✅ Acceptance Criteria

- The Python script is named `decorators.py`.
- The script demonstrates:
  - Defining a simple decorator.
  - Applying the decorator to a function.
  - Using decorators with parameters.

### 🛠️ Steps to Complete

1. **📁 Create a new Python file**: Name the file `decorators.py`.

2. **📝 Define a basic decorator**: Create a decorator function that prints a message before and after the execution of a function.
    ```python
    def simple_decorator(func):
        def wrapper():
            print("Before function call")
            func()
            print("After function call")
        return wrapper
    ```

3. **🔄 Apply the decorator**: Use the `@decorator_name` syntax to apply the decorator to a function.
    ```python
    @simple_decorator
    def greet():
        print("Hello!")
    ```

4. **📤 Print results**: Call the decorated function and observe the output.

5. **✏️ Use decorators with parameters**: Modify the decorator to accept parameters and log the execution time of a function.

6. **💬 Comment your code**: Ensure that each decorator and its usage are well-documented.

### Tips

- Decorators are powerful for modifying or extending function behavior without modifying the function itself.
- Use `functools.wraps` in decorators to preserve the metadata of the original function.

---

## Exercise 2: Python Generators

### ✅ Acceptance Criteria

- The Python script is named `generators.py`.
- The script demonstrates:
  - Defining a basic generator function.
  - Using `yield` to produce values.
  - Iterating over generator objects.
  - Understanding the advantages of generators over lists.

### 🛠️ Steps to Complete

1. **📁 Create a new Python file**: Name the file `generators.py`.

2. **📝 Define a basic generator**: Create a generator function that yields a sequence of numbers.
    ```python
    def count_up_to(max):
        count = 1
        while count <= max:
            yield count
            count += 1
    ```

3. **🔄 Use the generator**: Iterate over the generator using a loop or `next()`.
    ```python
    for number in count_up_to(5):
        print(number)
    ```

4. **📊 Compare with lists**: Show how generators can handle large sequences efficiently without storing all values in memory.

5. **✏️ Comment your code**: Ensure that each section of the script is properly commented for clarity.

### Tips

- Generators are a memory-efficient way to handle large datasets because they yield items one at a time instead of storing them all in memory.
- Use the `next()` function to manually retrieve items from a generator.

---

## Additional Resources

- [Python Decorators Documentation](https://docs.python.org/3/glossary.html#term-decorator)
- [Real Python: Python Decorators](https://realpython.com/primer-on-python-decorators/)
- [GeeksforGeeks: Python Decorators](https://www.geeksforgeeks.org/decorators-in-python/)
- [Python Generators Documentation](https://docs.python.org/3/howto/pyporting.html#generators)
- [Real Python: Python Generators](https://realpython.com/introduction-to-python-generators/)
- [GeeksforGeeks: Python Generators](https://www.geeksforgeeks.org/python-generators/)

---

## Submission

Once you complete the tasks, submit the `decorators.py` and `generators.py` files to your instructor.

Happy coding cyberpunks and brainiacs!