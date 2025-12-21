# Data Structures
# Lists, Dictionaries, Tuples, Sets
list_example = [1, 2, 3, 4, 5, 5, 5, ]
dict_example = {
    "name": "Alice", 
    "age": 25, 
    "cgpa": 3.8,    
}
tuple_example = (1, 2, 3)
set_example = {1, 2, 3, 4, 5, 5, 5}  # Duplicates will be removed from a set


print("List Example:", list_example)
print("Dictionary Example:", dict_example)
print("Tuple Example:", tuple_example)
print("Set Example:", set_example)

# Accessing elements
print("Accessing elements:")
print("First element of list:", list_example[0])
print("Value for 'name' in dictionary:", dict_example["name"])

list_example.append(6)
set_example.add(6)
