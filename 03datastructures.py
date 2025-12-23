"""This script demonstrates basic data structures in Python.

It covers:
1. Lists
2. Tuples
3. Dictionaries
4. Sets

The script provides examples of how to create, access, and manipulate these data structures.

The most comomonly used data structures in Python are lists and dictionaries.
"""

print("\n")
print("=" * 80)
print("Demonstrating basic data structures in Python")
print("=" * 80, end="\n\n")

##########################################################################
# 1. Lists
print("1. Lists")
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)
fruits.append("date")  # Adding an item to the list
print("After appending 'date':", fruits)
print("Accessing the first fruit:", fruits[0])
print("Accessing the last fruit:", fruits[-1])
print("Accessing a slice of the list (first two fruits):", fruits[0:2])
print("Accessing a slice of the list (last two fruits):", fruits[-2:])
print("Length of the list:", len(fruits))
fruits.remove("banana")  # Removing an item from the list
print("After removing 'banana':", fruits)
fruits.pop()  # Removing the last item
print("After popping the last item:", fruits)
print("\n")
# Explanation:
# Lists are mutable, meaning we can change their content (e.g., append, remove items).
# Lists are ordered collections, so the order of elements is preserved.


list_example = [1, 5, 3, 2, 4]
print("Example list:", list_example)

# list can be sorted and reversed
list_example.sort()  # Sorting the list
print("Sorted list:", list_example)
list_example.reverse()  # Reversing the list
print("Reversed list:", list_example)
print("\n" + "-" * 40 + "\n")


##########################################################################
# 2. Tuples
print("2. Tuples")
coordinates = (10, 20)
print("Original tuple:", coordinates)
print("Accessing the first coordinate:", coordinates[0])
print("Accessing the second coordinate:", coordinates[1])
# Tuples are immutable, so we cannot append or modify them
print("\n" + "-" * 40 + "\n")


##########################################################################
# 3. Dictionaries
print("3. Dictionaries")
person = {"name": "Alice", "age": 30, "city": "New York"}
print("Original dictionary:", person)
print("Accessing the name:", person["name"])
person["age"] = 31  # Updating age
print("After updating age to 31:", person)
person["profession"] = "Engineer"  # Adding a new key-value pair
print("After adding profession:", person)
print("\n" + "-" * 40 + "\n")


##########################################################################
# 4. Sets
print("4. Sets")
unique_numbers = {1, 2, 3, 4, 5}
print("Original set:", unique_numbers)
unique_numbers.add(6)
print("After adding 6:", unique_numbers)
unique_numbers.add(3)  # Adding a duplicate, will have no effect
print("After trying to add duplicate 3:", unique_numbers)
# Sets does not allow duplicates
# Sets do not support indexing, so we cannot access elements by position
print("Checking membership (is 4 in the set?):", 4 in unique_numbers)
print("Checking membership (is 10 in the set?):", 10 in unique_numbers)
print("\n" + "-" * 40 + "\n")
