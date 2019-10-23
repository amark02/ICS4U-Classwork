class Food:
    """Food Class

    Attributes:
        name (str): name of the food
        cost (int): price of the food
        nutrition (int): the nutrtional value of the food
    """
    def __init__(self, name: str, cost: int, nutrition: int):
        """Create a Food object.

        Args:
            name: name of the food
            cost: price of the food
            nutrition: nutritional value of the food
        """
        self.name = name
        self.cost = cost
        self.nutrition = nutrition


class Dog:
    """Thing that goes "roof"

    Attributes:
        breed (str): the breed of the dog
        name (str): the name of the dog
        happiness (int): how happy the dog is. defaults to 100
    """
    def __init__(self, breed: str, name: str):
        """Create a dog object

        Args:
            breed: breed of the dog
            name: name of the dog
        """
        self.breed = breed
        self.name = name
        self.happiness = 100

    def eat(self, food: Food):
        """ Get the dog to eat some food.

        Increasing the dog's happiness by 10% of the food eaten

        Args:
            food: type of food for the dog to eat
        """
        happiness_increase = food.nutrition * 0.1
        self.happiness += happiness_increase

    def bark(self):
        """ The dog will bark"""
        print("RUFF RUFF!")

    def __str__(self) -> str:
        return f"{self.name}, happiness: {self.happiness}"
        

def main():
    sausage = Food("Polish Sauage", 10, 100)
    fido = Dog("Husky", "Fido")

    print(fido)

    fido.eat(sausage)

    print(fido)

    fido.bark()

    print(fido)

if __name__ == "__main__":
    main()