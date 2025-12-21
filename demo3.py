
class Share:
    # These are variables that each instance of Share will have
    name: str
    symbol: str
    price: float
    quantity: int

    def __init__(self, name: str, symbol: str, price: float, quantity: int):
        self.name = name
        self.symbol = symbol
        self.price = price
        self.quantity = quantity

class Student:
    # Note that there are no variables defined here
    # They will be created in the constructor
    # All variables are instance variables
    # They are unique to each instance of Student
    # Use this style for agents where attributes are unique to each agent

    def __init__(self, name: str = "", age: int = 0, cgpa: float = 0.0):
        self.name: str = name
        self.age: int = age
        self.cgpa: float = cgpa







list1 = [1, 2, 3, 4, 5]

class Person:

    friends: list[str] = []

    def __init__(self, name: str):
        self.name = name

p1 = Person("Alice")
p2 = Person("Bob")
p3 = Person("Charlie")

print(p1.name)
print(p2.name)
print(p3.name)

p1.friends.append("David")
print(p1.friends)
print(p2.friends)
print(p3.friends)

