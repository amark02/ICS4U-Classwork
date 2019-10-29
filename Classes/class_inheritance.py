""" Inheritance """

"""
Cat
===
name: str
breed: str
-----
speak() -> void


Dog
===
name: str
breed: str
-----
speak() -> void
"""

class Animal:
    sound = "Generic animal sound"

    def __init__(self, name: str):
        self.name = name

    def speak(self):
        print(Animal.sound)
    
    def __str__(self):
        return f"{self.name}"

    @classmethod
    def speak(cls):
        print(cls.sound)

class Cat(Animal):
    sound = "Meow"

    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed
    
    def __str__(self):
        return super().__str__() + f", breed: {self.breed}"

    def speak(self):
        print(Cat.sound)


class Dog(Animal):
    sound = "Woof"

    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(Dog.sound)

class Chipmunk(Animal):
    sound = "Squeek"


def main():
    d = Dog("Fluffy", "Husky")
    print(d)
    d.speak()

    c = Cat("Oscar", "Tabby")
    print(c)
    c.speak()

    cm = Chipmunk("Alvin")
    print(cm)
    cm.speak()

if __name__ == "__main__":
    main()
