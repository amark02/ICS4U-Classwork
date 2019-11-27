"""
Complete the provided spreadsheet by changing the values in this program
according to the spreadsheet and record the results.
"""


import timeit
from typing import List


def linear_search(target: int, data: List) -> int:
    for i, num in enumerate(data):
        if num == target:
            return i
    
    return -1

"""
def binary_search(target: int, data: List) -> int:
    start = 0
    end = len(data)-1

    while end >= start:
        mid = (start + end) // 2
        if target == data[mid]:
            return mid
        elif target > data[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1
"""

DATASET_SIZE = 10**1
NUMBER = 1
SEARCH_TARGET = 10**1 // 2

dataset = range(DATASET_SIZE)

result = timeit.timeit(
    "linear_search(SEARCH_TARGET, dataset)",
    number=NUMBER,
    globals=globals())

print(result)