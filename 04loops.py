"""This script demonstrates loops in Python."""

print("\n")
print("=" * 80)
print("Demonstrating loops in Python")
print("=" * 80, end="\n\n")

##########################################################################
# 1. For Loop
print("1. For Loop")
fruits = ["apple", "banana", "cherry"]
print("Fruits in the list:")
for fruit in fruits:
    print(fruit)
print("\n" + "-" * 40 + "\n")

##########################################################################
# 2. While Loop
print("2. While Loop")
count = 0
print("Counting from 0 to 4:")
while count < 5:
    print(count)
    count += 1
print("\n" + "-" * 40 + "\n")

##########################################################################
# 3. Looping through a range of numbers
print("3. Looping through a range of numbers")
print("Numbers from 0 to 9:")
for i in range(10):  # 0 to 9
    print(i)
print("\n" + "-" * 40 + "\n")

##########################################################################
# 4. Nested Loops
print("4. Nested Loops")
print("Multiplication table (1 to 3):")
for i in range(1, 4):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  # New line after each row

print("\n" + "-" * 40 + "\n")

##########################################################################
# 5. Using break and continue
print("5. Using break and continue")
print("Demonstrating break and continue in a loop:")
for num in range(10):
    if num == 5:
        print("Breaking the loop at 5")
        break  # Exit the loop when num is 5
    if num % 2 == 0:
        print(f"Skipping even number: {num}")
        continue  # Skip even numbers
    print(f"Odd number: {num}")
print("\n" + "-" * 40 + "\n")

##########################################################################
# 6. Looping through a dictionary
print("6. Looping through a dictionary")
person = {"name": "Alice", "age": 30, "city": "New York"}
print("Person details:")
for key, value in person.items():
    print(f"{key}: {value}")
print("\n" + "-" * 40 + "\n")

##########################################################################
# 7. List Comprehensions
print("7. List Comprehensions")
squares = [x**2 for x in range(10)]
print("Squares of numbers from 0 to 9 using list comprehension:")
print(squares)
print("\n" + "-" * 40 + "\n")

# List comprehensions can also include conditions
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Squares of even numbers from 0 to 9 using list comprehension:")
print(even_squares)
print("\n" + "-" * 40 + "\n")

##########################################################################
# 8. Looping through different data structures
print("8. Looping through different data structures")
data_structures = [
    [1, 2, 3],  # List
    (4, 5, 6),  # Tuple
    {"a": 7, "b": 8},  # Dictionary
    "hello",  # String
]
for data in data_structures:
    print(f"Looping through: {data}")
    for item in data:
        print(item)
    print()  # New line after each data structure
print("\n" + "-" * 40 + "\n")

# Note:
# looping throuhg a dictionary iterates over its keys by default.
# To get values, use .values() and for key-value pairs, use .items().

# Looping through a string iterates over each character in the string.
print("End of loops demonstration.")
