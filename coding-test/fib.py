def fibonacci(n):
    _sum = 0
    fib1 = 0
    fib2 = 1
    height = 0
    for _ in range(2, n):
        _sum = fib1 + fib2
        fib1 = fib2
        fib2 = _sum
        height += _sum
    return height


print(fibonacci(6))
"""
n = 5, _sum = fib1 + fib2, fib1 = 0, fib2 = 1, height = 0
i = 2, _sum = 1, fib1 = 1, fib2 = 1, height = 1
i = 3, _sum = 2, fib1 = 1, fib2 = 2, height = 3
i = 4, _sum = 3, fib1 =2, fib2 = 3, height = 6

"""
