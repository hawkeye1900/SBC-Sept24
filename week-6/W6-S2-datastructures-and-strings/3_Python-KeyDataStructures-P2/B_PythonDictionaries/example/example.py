# ----------------------------
# Python Dictionaries
# ----------------------------

# Dictionaries in Python are collections of key-value pairs.
# They are unordered, mutable, and do not allow duplicate keys.

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print("Original Dictionary:", my_dict)

# ----------------------------
# Accessing Dictionary Values
# ----------------------------

# Accessing values using keys
print("Name:", my_dict["name"])  # Output: Name: Alice
print("Age:", my_dict["age"])    # Output: Age: 25

# ----------------------------
# Updating Dictionary Values
# ----------------------------

# Updating the value associated with an existing key
my_dict["age"] = 26
print("Updated Dictionary:", my_dict)  # Output: Updated Dictionary: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# ----------------------------
# Adding New Key-Value Pairs
# ----------------------------

# Adding a new key-value pair to the dictionary
my_dict["email"] = "alice@example.com"
print("Dictionary after adding email:", my_dict)  # Output: Dictionary after adding email: {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}

# ----------------------------
# Removing a Key-Value Pair
# ----------------------------

# Removing a key-value pair using the `del` keyword
del my_dict["city"]
print("Dictionary after removing city:", my_dict)  # Output: Dictionary after removing city: {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}

# ----------------------------
# Iterating Through Keys and Values
# ----------------------------

# Displaying dictionary keys, values, and items
print("Keys:", my_dict.keys())   # Output: Keys: dict_keys(['name', 'age', 'email'])
print("Values:", my_dict.values())  # Output: Values: dict_values(['Alice', 26, 'alice@example.com'])
print("Items:", my_dict.items())  # Output: Items: dict_items([('name', 'Alice'), ('age', 26), ('email', 'alice@example.com')])

# ----------------------------
# Handling Non-Existent Keys
# ----------------------------

# Note: Accessing a non-existent key will raise a KeyError.
# Uncommenting the following line will cause an error
# print(my_dict["non_existent_key"])  # KeyError: 'non_existent_key'