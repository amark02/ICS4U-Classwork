
class Person:
    #Functions inside classes are called methods
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Jeff", 34)
p2 = Person("Sally", 55)

print(p.name, p.age)
print(p2.name, p2.age)


