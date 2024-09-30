# ----------------------------
# Python JSON Objects
# ----------------------------

import json

# JSON (JavaScript Object Notation) is a lightweight format for storing and transporting data.
# Python's `json` module provides functions to work with JSON data.

# ----------------------------
# Parsing JSON Data
# ----------------------------

# Example JSON data as a string
json_data = '{"name": "Alice", "age": 25, "city": "New York"}'

# Parsing JSON data into a Python dictionary
python_dict = json.loads(json_data)
print("Parsed JSON into Python Dictionary:", python_dict)
# Output: Parsed JSON into Python dictionary: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# ----------------------------
# Converting Python Dictionary to JSON
# ----------------------------

# Converting a Python dictionary to JSON format
json_output = json.dumps(python_dict, indent=4)
print("Python Dictionary Converted to JSON:")
print(json_output)
# Output: Python dictionary converted to JSON:
# {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }

# ----------------------------
# Reading JSON Data from a File
# ----------------------------

# Reading JSON data from a file
# Ensure that 'data.json' exists in the same directory
with open('data.json', 'r') as file:
    file_data = json.load(file)
    print("Data Read from JSON File:", file_data)
# Ensure 'data.json' exists in your directory or create it for testing

# ----------------------------
# Writing JSON Data to a File
# ----------------------------

# Writing JSON data to a file
with open('output.json', 'w') as file:
    json.dump(python_dict, file, indent=4)
    print("Data Written to output.json")

# Note: Ensure that 'data.json' file exists in the same directory for reading.
# Handle exceptions if the file is not found or other I/O errors occur.