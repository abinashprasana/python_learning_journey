"""
Logger + Timer Decorator

Author: Abinash Prasana

This program demonstrates the use of Python decorators to:
- Log function calls
- Measure execution time

It wraps target functions to print the function name, log when it was called, and report how long it took to run.
"""

import time
def log_and_timer(func):
    def wrapper(*args, **kwargs):
        print(f"\n[LOG] calling function: {func.__name__}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"\n[LOG] Function: {func.__name__} executed in {end_time - start_time} seconds")
        return result
    return wrapper

@log_and_timer
def greet(name):
    print(f"Hello, {name}!")

@log_and_timer
def calculate_sum(n):
    total = 0
    for i in range(n):
        total += i
    print(f"Sum of number from to {n-1} is {total}")
    return total

greet("Abby")
calculate_sum(2000)