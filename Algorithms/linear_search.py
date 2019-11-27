from typing import List


# Linear Search
# 1. Basic linear search
# 2. Get last occurance of a value
# 3. Get list of all occurances

def linear_search(target: int, numbers: List[int]) -> int:
    """Search for a target value.

    Args:
        target: The int to search for.
        numbers: list of numbers.
    Returns: 
        Index locaiton of the found target number. -1 for not found.
    """
    for i, num in enumerate(numbers):
        if num == target:
            return i
    return -1

def test_linear_search():
    assert linear_search(5, []) == -1
    assert linear_search(5, [5]) == 0
    assert linear_search(5, [1, 2, 3, 4, 5]) == 4
    assert linear_search(5, [2, 5, 2]) == 1
    assert linear_search(5, [6, 5, 5]) == 1, 2

