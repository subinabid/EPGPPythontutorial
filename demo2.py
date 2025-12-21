from sys import argv

script, a, b = argv

def addNumbers(x, y):
    """Add two numbers and print the result."""
    result = float(x) + float(y)
    print("HI")
    print(result)
    print(f"The sum of {x} and {y} is: {result}")
    print("The sum of " + x + " and " + y + " is: " + str(result))

print("Script name:", script)
addNumbers(a, b)