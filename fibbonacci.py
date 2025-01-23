#This uses the concept of memoization, allows for larger computations

from typing import Dict
memo: Dict[int, int] = {0:0, 1:1}


def fib(n):
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    
    return memo[n]
#_____________________________________

#This funtion does the same thing, just using python's built in caches
from functools import lru_cache

@lru_cache(maxsize=None)
def fib2(n):
    if n < 2:
        return n
    return fib2(n-2) + fib2(n-1)

#_______________________________________

#Most efficient, just an iterative approach, uses tuple unpacking
def fib3(n):
    if n == 0:
        return n
    last = 0
    next = 1
    
    for _ in range(1, n):
        last, next = next, last + next
    return next


    
   



if __name__ == "__main__":
    print(fib3(50))
