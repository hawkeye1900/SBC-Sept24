# ----------------------------
# Python Regular Expressions
# ----------------------------

import re

# Defining regex patterns

# Pattern to match one or more digits
pattern = r'\d+'

# ----------------------------
# Searching for Patterns
# ----------------------------

# Searching for the first occurrence of the pattern
text = 'The price is 100 dollars'
match = re.search(pattern, text)
if match:
    print("First match:", match.group())  # Output: First match: 100

# ----------------------------
# Finding All Matches
# ----------------------------

# Finding all occurrences of the pattern
text = 'The price is 100 dollars and 200 euros'
all_matches = re.findall(pattern, text)
print("All matches:", all_matches)  # Output: All matches: ['100', '200']

# ----------------------------
# Replacing Text
# ----------------------------

# Replacing all occurrences of the pattern with 'XX'
replaced_text = re.sub(pattern, 'XX', text)
print("Text after replacement:", replaced_text)  # Output: Text after replacement: The price is XX dollars and XX euros

# ----------------------------
# Example Usage of Regular Expressions
# ----------------------------

# Validating a phone number format (e.g., (123) 456-7890)
phone_pattern = r'\(\d{3}\) \d{3}-\d{4}'
phone_number = '(123) 456-7890'
if re.match(phone_pattern, phone_number):
    print("Phone number is valid.")
else:
    print("Phone number is invalid.")

# Regular expressions are powerful tools for text processing and pattern matching.
# Understanding regex syntax and functions is essential for complex text manipulation tasks.