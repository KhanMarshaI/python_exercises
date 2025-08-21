# Implement fib(n) with @lru_cache(maxsize=None) and time it against a non-cached version
from functools import lru_cache
from time import perf_counter

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

@lru_cache(maxsize=None)
def fib_cache(n):
    if n <= 1:
        return n
    return fib_cache(n-1) + fib_cache(n-2)

t1_start = perf_counter()
fib(37)
t1_stop = perf_counter()

print("Non-cache time:", t1_stop - t1_start)

t2_start = perf_counter()
fib_cache(37)
t2_stop = perf_counter()

print("Cache Time:", t2_stop - t2_start)