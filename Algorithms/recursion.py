
"""
- Recursion: having a function call itself
- Base case: What is the final end-point of this algorithm?
- Recursive case: Call the function again. (algorithm not complete)
"""

def sum_up_to(n: int) -> int:
    if n == 1: # base case
        return 1 

    print(n)

    # recursive case
    return n + sum_up_to(n-1)

print(sum_up_to(3))