from typing import List, Dict

"""
# Factorial
def factorial(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n * factorial(n-1)
print(factorial(1))
print(factorial(2))
print(factorial(3))
"""
"""
# bunnyEars
def bunnyEars(n: int) -> int:
    if n == 0:
        return 0
    return 2 + bunnyEars(n-1)
print(bunnyEars(0))
print(bunnyEars(1))
print(bunnyEars(2))
"""
"""
# Fibonacci
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
"""
"""
# strCount
def str_count(string: str, ksub: str) -> int:
    if string == "":
        return 0
    if string.startswith(sub):    # other way string[:len(sub)]
        return 1 + str_count(string[len(sub):], sub)
    return 0 + str_count(string[1:], sub)
"""
"""
# arrary2020
def arrary_2020(numbers: List[int]) -> bool:
    if i > len(numbers) - 2:
        return False
    
    if numbers[i] * 10 == numbers[i+1]:
        return True
    
    return False or array_2020(numbers, i+1)
"""
"""
# strDist
def str_dist(string: str, sub: str) -> int:
    if string == "":
        return 0
"""
"""
# triangle
def triangle(row: int) -> int:
    if row == 0:
        return 0
    return row + triangle(row-1)
print(triangle(0))
print(triangle(1))
print(triangle(2))
"""
"""
# bunnyEars2
def bunnyEars2(n: int) -> int:
    ears = 0
    if n == 0:
        return 0
    if n == 1:
        return 2
    if n % 2 == 0:
        ears = 3
    else: 
        ears = 2
    return ears + bunnyEars2(n-1)  
print(bunnyEars2(0)) 
print(bunnyEars2(1)) 
print(bunnyEars2(2))
"""
"""
# sumDigits
def sumDigits(n: int) -> int:
    if n < 10:
        return n
    return n % 10 + sumDigits(n//10)
print(sumDigits(126))
print(sumDigits(49))
print(sumDigits(12))
"""
"""
# count7
def count7(n: int) -> int:
    if n < 10:
        if n == 7:
            return 1
        else:
            return 0
    if n % 10 == 7:
        return 1 + count7(n//10)
    else:
        return count7(n//10)  
print(count7(717))
print(count7(7))
print(count7(123))
"""

# count8
def count8(n: int) -> int:
    if n < 10:
        if n == 8:
            return 1
        else:
            return 0
    if n % 10 == 8:
        if n % 100:
            return 2 + count8(n//10)
        else:
            return 1 + count8(n//10)
    else: 
        return count8(n//10)
print(count8(8))
print(count8(818))
print(count8(8818))