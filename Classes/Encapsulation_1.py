
class Person:
    def __init__(self, name: str, age: int):
        self.set_name(name)
        self._age = age
    
    def get_age(self):
        #age = time_now - self.date_of_birth
        return self._age

    def set_age(self, value: int):
        self._age = value

    def get_name(self):
        return self._first_name + " " + self._last_name

    def set_name(self, value: str):
        first, last = value.split(" ")
        self._first_name = first
        self._last_name = last

# /\ library author's code /\
# \/ OUR CODE \/

VOTING_AGE = 18

p = Person(name = "Jeff Foxworthy", age = 35)

if p.get_age() >= VOTING_AGE:
    print(f"{p.get_name()} can vote")