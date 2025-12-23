"""Accepting input from the terminal.

This script demonstrates how to accept different types of input from the terminal
using the input() function in Python.

It covers:
1. Accepting string input
2. Accepting numerical input and performing calculations
3. Accepting multiple inputs in one line

Note: This script is intended to be run in a terminal or command prompt.
"""

# Accepting input from the terminal
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello, {name}! You are {age} years old.")

# Accepting numerical input and performing calculations
print("\n")
print("Let's add two numbers.")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is: {sum_result}")

# Accepting multiple inputs in one line
print("\n")
print("Now, enter three numbers in a line to multiply them.")
numbers = input("Enter three numbers separated by spaces: ")
num_list = numbers.split()
num1, num2, num3 = map(float, num_list)
product = num1 * num2 * num3
print(f"The product of {num1}, {num2}, and {num3} is: {product}")
