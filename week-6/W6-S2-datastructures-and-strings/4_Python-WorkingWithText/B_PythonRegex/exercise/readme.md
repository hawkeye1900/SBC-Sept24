# 🧩 Python Regular Expressions

## 🎯 Challenge

Your challenge is to create a Python script that demonstrates working with regular expressions (regex). Focus on pattern matching, searching, and replacing text using regex in Python.

## 📚 Key Learnings

By completing this exercise, you will learn:

- How to use regular expressions to match patterns in text.
- How to search for patterns within strings.
- How to replace text based on regex patterns.

## 👤 User Story

As a Python developer, I want to understand how to use regular expressions for complex text processing tasks, such as validating input, searching for patterns, and replacing substrings.

## ✅ Acceptance Criteria

- The Python script is named `regular_expressions.py`.
- The script demonstrates:
  - Matching patterns with regex.
  - Searching and finding patterns in text.
  - Replacing text based on regex patterns.

## 🛠️ Steps to Complete

1. **📁 Create a new Python file**: Name the file `regular_expressions.py`.

2. **📜 Import the `re` module**: Use `import re` to work with regular expressions.

3. **🔍 Define a pattern**: Create a regex pattern to search for. For example, `pattern = r'\d+'` to match one or more digits.

4. **🔎 Search for patterns**: Use `re.search()` to find the first occurrence of the pattern in a string. For example, `match = re.search(pattern, 'The price is 100 dollars')`.

5. **🔄 Find all matches**: Use `re.findall()` to find all occurrences of the pattern in a string. For example, `all_matches = re.findall(pattern, 'The price is 100 dollars and 200 euros')`.

6. **✏️ Replace text**: Use `re.sub()` to replace text matching the pattern. For example, `replaced_text = re.sub(pattern, 'XX', 'The price is 100 dollars')`.

7. **📤 Print results**: Print the results of each operation to verify that the regex operations work as expected.

8. **💬 Comment your code**: Ensure that each section of the script is properly commented for clarity.

## Tips

- Regular expressions can be complex; start with simple patterns and gradually build more complex ones.
- Use online regex testers to experiment with patterns.

## Additional Resources

- [Python re Module Documentation](https://docs.python.org/3/library/re.html)
- [Regex101: Online Regex Tester](https://regex101.com/)
- [Regexr: Online Regex Tester and Debugger](https://regexr.com/)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

## Submission

Once you complete the task, submit the `regular_expressions.py` file to your instructor.

Happy coding technophiles!