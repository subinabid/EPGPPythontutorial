from sys import argv

script, name = argv

def countName(name):
    """Count the number of characters in a name."""
    print("Number of characters in the name:", len(name))

print("Script name:", script)
countName(name)  

