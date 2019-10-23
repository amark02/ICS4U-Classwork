"""
ENCAPSULATION

Basic definition: protecting your object's attributes.
"""


class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self._age = age

    def set_age(self, age: int):
        # verify age value
        if type(age) != int:
            raise ValueError("Age must be an integer.")
        self._age = age

    def get_age(self) -> int:
        return self._age

    def age_in_5_years(self):
        return self._age + 5

s = Student("Sally", 15)

print(s.get_age())