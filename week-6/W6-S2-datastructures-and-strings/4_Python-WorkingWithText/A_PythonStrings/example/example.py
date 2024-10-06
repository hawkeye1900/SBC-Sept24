# ----------------------------
# Python Strings
# ----------------------------

# Creating and initializing strings

# Single quotes
single_quote_str = 'Hello, World!'
print("Single Quote String:", single_quote_str)

# Double quotes
double_quote_str = "Hello, World!"
print("Double Quote String:", double_quote_str)

# Triple quotes (for multi-line strings)
triple_quote_str = """Hello,
World!
This is a multi-line string."""
print("Triple Quote String:", triple_quote_str)

# ----------------------------
# String Concatenation
# ----------------------------

# Concatenating strings using the + operator
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print("Concatenated String:", message)

# ----------------------------
# String Slicing
# ----------------------------

# Slicing strings to extract substrings
text = "Python Programming"
first_word = text[0:6]  # Extracts "Python"
second_word = text[7:]  # Extracts "Programming"
print("First Word:", first_word)
print("Second Word:", second_word)

# ----------------------------
# String Formatting
# ----------------------------

# Using f-strings for formatting
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print("Formatted String (f-string):", formatted_string)

# Using format() method for formatting
formatted_string2 = "My name is {} and I am {} years old.".format(name, age)
print("Formatted String (format method):", formatted_string2)

# ----------------------------
# Common String Methods
# ----------------------------

# Convert to upper case
upper_case_str = text.upper()
print("Upper Case String:", upper_case_str)

# Convert to lower case
lower_case_str = text.lower()
print("Lower Case String:", lower_case_str)

# Strip whitespace
whitespace_str = "   Extra spaces   "
stripped_str = whitespace_str.strip()
print("Stripped String:", stripped_str)

# Replace substring
replaced_str = text.replace("Python", "JavaScript")
print("Replaced String:", replaced_str)

# ----------------------------
# Example Usage of Strings
# ----------------------------

# Creating a message using string methods
base_message = " Hello World "
formatted_message = base_message.strip().upper()
print("Formatted Message:", formatted_message)


# Strings are fundamental in Python for handling and manipulating text.
# Understanding string operations is crucial for text processing and formatting tasks.