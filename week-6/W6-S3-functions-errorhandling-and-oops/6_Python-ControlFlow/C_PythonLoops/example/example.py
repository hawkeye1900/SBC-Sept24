# ----------------------------
# Python Loops
# ----------------------------

# 1. For Loop with Lists
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
print("Fruits list:")
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

# 2. For Loop with Tuples
# Iterating over a tuple
numbers = (1, 2, 3, 4, 5)
print("\nNumbers tuple:")
for number in numbers:
    print(number)
# Output:
# 1
# 2
# 3
# 4
# 5

# 3. For Loop with Ranges
# Iterating over a range of numbers
print("\nRange from 0 to 4:")
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# 4. While Loop
# Using a while loop to count from 1 to 3
count = 1
print("\nCounting with while loop:")
while count <= 3:
    print(count)
    count += 1
# Output:
# 1
# 2
# 3

# 5. Break Statement
# Exiting a loop early with break
print("\nLoop with break statement:")
for i in range(5):
    if i == 3:
        break
    print(i)
# Output:
# 0
# 1
# 2

# 6. Continue Statement
# Skipping an iteration with continue
print("\nLoop with continue statement:")
for i in range(5):
    if i % 2 == 0:
        continue
    print(i)
# Output:
# 1
# 3

# Loops are essential for repeating tasks and iterating over sequences.
# They help in efficiently processing data and controlling the flow of execution.