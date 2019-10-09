class Person:
    #Functions inside classes are called methods
    def __init__(self, name, age):
        self.name = name
        self.age = age

"""
people = [
    Person("a", 1),
    Person("b", 2),
    Person("c", 3),
    Person("d", 4),
    Person("e", 5)
]

for person in people:
    print(person.name)(

makes a list of people and prints out each person's name
"""

people = []

for name, age in [("Jeff", 34), ("Sally", 55), ("Jim", 22)]:
    p = Person(name, age)
    people.append(p)

for person in people:
    print(person.name)

