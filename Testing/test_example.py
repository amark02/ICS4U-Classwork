"""
def test_testing():
    assert True == True

    just makes sure pytest is working on this file
"""

def add(a, b):
    return a + b

def test_add():
    assert add(1, 1) == 2
    assert add(3, 4) == 7
