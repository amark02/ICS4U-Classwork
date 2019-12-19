from typing import List

"""
def contain_6(array: List[int], x: int) -> bool:
    if x == len(array):
        return False
    return array[x] == 6 or contain_6(array, x + 1)

print(contain_6([1, 6, 4], 0))
print(contain_6([1, 4], 0))
print(contain_6([6], 0))
"""

"""
def sep_char(str_: str, symbol: str) -> str:
    if len(str_) <= 1:
        return str_
    return str_[0] + symbol + sep_char(str_[1:], symbol)

print(sep_char("hello", "*"))
print(sep_char("abc", "."))
print(sep_char("ab", "/"))
"""

def only_inside(str_: str) -> str:
    if str_