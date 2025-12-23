"""This script demonstrates functions in Python.

It covers:
1. Defining functions
2. Function parameters and return values
3. Default parameters
4. Variable-length arguments
5. Lambda functions
"""

print("\n")
print("=" * 80)
print("Demonstrating functions in Python")
print("=" * 80, end="\n\n")

##########################################################################
# 1. Defining functions
print("1. Defining functions")


def greet():
    """A simple function that greets the user."""
    print("Hello! Welcome to the Python functions tutorial.")


greet()  # Calling the function
print("\n" + "-" * 40 + "\n")

##########################################################################
# 2. Function parameters and return values
print("2. Function parameters and return values")


def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


result = add(5, 3)  # Calling the function with arguments andstoring the return value
print("The sum of 5 and 3 is:", result)
print("\n" + "-" * 40 + "\n")

##########################################################################
# 3. Default parameters
print("3. Default parameters")


def power(base, exponent=2):
    """Returns the base raised to the power of exponent. Default exponent is 2."""
    return base**exponent


print("5 squared is:", power(5))  # Using default exponent
print("2 cubed is:", power(2, 3))  # Providing both parameters
print("\n" + "-" * 40 + "\n")
##########################################################################

# 4. Variable-length arguments
print("4. Variable-length arguments")


def multiply(*args):
    """Returns the product of all given numbers."""
    product = 1
    for num in args:
        product *= num
    return product


print("Product of 2, 3, and 4 is:", multiply(2, 3, 4))
print("Product of 5 and 6 is:", multiply(5, 6))
print("\n" + "-" * 40 + "\n")
##########################################################################

# 5. Lambda functions
print("5. Lambda functions")
square = lambda x: x**2  # A lambda function to square a number
print("Square of 6 is:", square(6))
print("\n" + "-" * 40 + "\n")

print("End of functions demonstration.")
