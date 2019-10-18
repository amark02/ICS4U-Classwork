class Food:
    """
    Attrs:
        name (str): name of the food
        cost (int): price of the food
        nutrition (int): the nutrtional value of the food
    """
    def __init__(self, name: str, cost: int, nutrition: int):
        self.name = name
        self.cost = cost
        self.nutrition = nutrition
    
class Dog:
    """
    Attrs:
        breed (str): the breed of the dog
        name (str): the name of the dog
        happiness (int): how happy the dog is
    """
    def __init__(self, breed: str, name: str, happiness: int):
        self.breed = breed
        self.name = name
        self.happiness = happiness

    def eat(self, Food):
        self.happiness = round(0.1 * Food.nutrition)

    def bark():
        print("RUFF RUFF!")

    def __str__(self):
        return f"{self.name}, happiness: {self.happiness}"

        
        
