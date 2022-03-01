def factorial(n):
    if n == 0:
        return 1
    if n < 2:
        return n

    return factorial(n-1) * n

print(factorial(6))