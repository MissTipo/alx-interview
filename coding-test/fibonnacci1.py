def fibonacci_sum(n):
    if n <= 0:
        return 0

    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return sum(fib_sequence[:n])


# Test the function
n = int(input("Enter a positive integer n: "))
result = fibonacci_sum(n)
print(
    f"The sum of the first {n} numbers in the Fibonacci sequence is: {result}")
