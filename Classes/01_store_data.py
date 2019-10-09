
class Person:
    pass


p = Person()
p.name = "Jeff"
p.eye_color = "Blue"

p2 = Person()

print(p)
print(p.name)
print(p.eye_color)

"""
print(p2.name)

gives an error since the object has no attribute of name
since you gave the other person an attribute on the fly
"""