# 🐍 Python Generators

## 🎯 Challenge

Your challenge is to create a Python script that demonstrates the usage of generators. Focus on defining basic generators, using them to iterate over sequences, and understanding their advantages.

## 📚 Key Learnings

By completing this exercise, you will learn:

- How to define and use generators in Python.
- The difference between generators and regular functions.
- How generators can be used to iterate over large sequences efficiently.

## 👤 User Story

As a Python developer, I want to understand how to use generators to create iterators that produce items on-the-fly, which is useful for working with large datasets or streams of data.

## ✅ Acceptance Criteria

- The Python script is named `generators.py`.
- The script demonstrates:
  - Defining a basic generator function.
  - Using `yield` to produce values.
  - Iterating over generator objects.
  - Understanding the advantages of generators over lists.

## 🛠️ Steps to Complete

1. **📁 Create a new Python file**: Name the file `generators.py`.

2. **📝 Define a basic generator**: Create a generator function that yields a sequence of numbers. For example:
    ```python
    def count_up_to(max):
        count = 1
        while count <= max:
            yield count
            count += 1
    ```

3. **🔄 Use the generator**: Iterate over the generator using a loop or `next()`. For example:
    ```python
    for number in count_up_to(5):
        print(number)
    ```

4. **📊 Compare with lists**: Show how generators can handle large sequences efficiently without storing all values in memory.

5. **✏️ Comment your code**: Ensure that each section of the script is properly commented for clarity.

## Tips

- Generators are a memory-efficient way to handle large datasets because they yield items one at a time instead of storing them all in memory.
- Use the `next()` function to manually retrieve items from a generator.

## Additional Resources

- [Python Generators Documentation](https://docs.python.org/3/howto/pyporting.html#generators)
- [Real Python: Python Generators](https://realpython.com/introduction-to-python-generators/)
- [GeeksforGeeks: Python Generators](https://www.geeksforgeeks.org/python-generators/)
- [W3Schools: Python Generators](https://www.w3schools.com/python/python_generators.asp)

## Submission

Once you complete the task, submit the `generators.py` file to your instructor.

Happy coding brainiacs!