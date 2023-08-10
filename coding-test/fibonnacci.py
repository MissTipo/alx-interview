"""
Write a function that takes a positive integer n as input and returns the sum of the first n
numbers in the Fibonacci sequence.
"""


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(6))
