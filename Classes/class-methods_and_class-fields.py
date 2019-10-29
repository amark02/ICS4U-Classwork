"""
- Class field
- Class method

- Inheritance
"""

"""
Create the following class:

Pizza
====
name: str
toppings: List[str]
------
__str__ -> str


- Create a main function and create some pizzas
- the __str__ method will be the following format: "{name}, toppings: {toppings}"
"""
from typing import List


class Pizza:
    num_pizzas = 0 # class field (variable)

    def __init__(self, name: str, toppings: List[str]):
        self.name = name
        self.toppings = toppings
        self.id = Pizza.num_pizzas
        Pizza.num_pizzas += 1
    
    def __str__(self) -> str:
        return f"{self.name}, toppings: {self.toppings}, id: {self.id}"

    @classmethod
    def pepperoni(cls):
        return cls("Pepperoni", ["cheese", "pepperoni"])
    
    @classmethod
    def cheese(cls):
        return cls("Cheese", ["cheese"])

    def add_toppings(self, toppings: List[str]):
        self.toppings += toppings
    

def main():
    pepperoni = Pizza.pepperoni()
    print(pepperoni)

    cheese = Pizza.cheese()
    print(cheese)

    cheese_another= Pizza.cheese()
    print(cheese_another)

    print(Pizza.num_pizzas)


if __name__ == "__main__":
    main()


