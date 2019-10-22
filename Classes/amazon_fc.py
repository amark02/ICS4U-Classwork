class Item:
    def __str__(self):
        return "Item Object"


class Cart:
    # add location field
    # add ID field
    def __init__(self):
        self.contents = []

    def __str__(self):
        return f"Cart ID"

    def add(self, item):
        pass

    def remove(self, item):
        self.contents.remove(item)

    def print_contents(self):
        print(self)
        for item in self.contents:
            print(item)


class Shelf:
    def add(self):

item = Item()
cart = Cart()

cart.add(item)

cart.print_contents()


cart.remove(item)




shelf.add("A3", item)
shelf.a3.add(item)


shelf.compartment["A3"].append(item)
shelf.compartment("A3").add(item)