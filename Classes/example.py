"""
a = 5
b = a # copies over the value

print(a) # 5
print(b) # 5

a = 10

print(a) # 10
print(b) # 5
"""

class Person:
    pass

a = Person()
b = a

print(a)
print(b)

b.name = "Jeff"

print(a.name)

del b

print(a)