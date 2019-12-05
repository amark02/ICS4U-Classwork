def fib(n: int):
    if n <= 1:
        return 0
    return fib(n-1) + fib(n-2)
fib(3)