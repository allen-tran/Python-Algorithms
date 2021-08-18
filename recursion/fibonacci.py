'''
Determine the value given an index within a fibonacci sequence
'''

def fibonacci(n):
    assert n >= 0 and int(n) == n, 'Fibonacci must be an integer that is greater than or equal to 0'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(-7))
