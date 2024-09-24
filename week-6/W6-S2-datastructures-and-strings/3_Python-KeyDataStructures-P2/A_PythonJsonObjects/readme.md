# 🐍 Python JSON Objects

## 🎯 Challenge

Your challenge is to create a Python script that demonstrates working with JSON (JavaScript Object Notation) data. Focus on parsing JSON data, accessing its elements, and converting between JSON and Python objects.

## 📚 Key Learnings

By completing this exercise, you will learn:

- How to parse JSON data in Python.
- How to access and manipulate JSON data.
- How to convert between JSON strings and Python objects (dictionaries).

## 👤 User Story

As a Python developer, I want to understand how to work with JSON data effectively for data interchange between systems and applications.

## ✅ Acceptance Criteria

- The Python script is named `json_objects.py`.
- The script demonstrates:
  - Parsing JSON data from a string.
  - Accessing and modifying JSON data.
  - Converting Python objects to JSON and vice versa.

## 🛠️ Steps to Complete

1. **📁 Create a new Python file**: Name the file `json_objects.py`.

2. **📜 Import the JSON module**: Use `import json` to work with JSON data.

3. **🔍 Define a JSON string**: Create a JSON string with some sample data. For example, `json_string = '{"name": "Alice", "age": 25, "city": "New York"}'`.

4. **🔄 Parse JSON data**: Use `json.loads()` to parse the JSON string into a Python dictionary. For example, `data = json.loads(json_string)`.

5. **🔗 Access JSON elements**: Demonstrate how to access elements in the parsed JSON data. For example, `data['name']`.

6. **✏️ Modify JSON data**: Show how to modify the values in the Python dictionary. For example, `data['age'] = 26`.

7. **🔄 Convert Python object to JSON**: Use `json.dumps()` to convert the Python dictionary back into a JSON string. For example, `json_data = json.dumps(data)`.

8. **📤 Print results**: Print the results of each operation to verify that the JSON operations work as expected.

9. **💬 Comment your code**: Ensure that each section of the script is properly commented for clarity.

## Tips

- JSON is a common data format for APIs and configuration files.
- Use `json.dumps()` with the `indent` parameter for pretty-printing JSON data.

## Additional Resources

- [Python JSON Documentation](https://docs.python.org/3/library/json.html)
- [Python JSON Tutorial](https://www.w3schools.com/python/python_json.asp)
- [Real Python: Working with JSON Data](https://realpython.com/python-json/)
- [GeeksforGeeks: Python JSON](https://www.geeksforgeeks.org/python-json/)

## Submission

Once you complete the task, submit the `json_objects.py` file to your instructor.


Happy coding devs!