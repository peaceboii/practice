import functools
import time

@functools.lru_cache(maxsize=None)
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

start_time = time.time()
fib(111)
end_time = time.time()
print(f"Execution time 1st: {end_time - start_time} seconds")

start_time = time.time()
fib(111)
end_time = time.time()
print(f"Execution time 2nd: {end_time - start_time} seconds")

