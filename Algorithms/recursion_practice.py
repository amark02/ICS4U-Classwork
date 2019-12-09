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

# strCount
def str_count(string: str, ksub: str) -> int:
    if string == "":
        return 0
    if string.startswith(sub):    # other way string[:len(sub)]
        return 1 + str_count(string[len(sub):], sub)
    return 0 + str_count(string[1:], sub)
