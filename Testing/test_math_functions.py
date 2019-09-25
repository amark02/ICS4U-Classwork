import math_functions #(don't need '.py' at the end)
# from math_functions import add, subtract (allows you to import certain functions)

# math_functions.add() (allows you to use the function from the other file)

def test_add():
    assert math_functions.add(1, 1) == 2
    assert math_functions.add(3, 5) == 8


def test_subract():
    assert math_functions.subract(5, 2) == 3