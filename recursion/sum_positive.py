'''
Find the sum of digits of a positive integer number using recursion
'''


def sum_positive(n):
    assert n >= 0 and int(n) == n, "Numbers must be postive and non-negative"
    if n == 0:
        return 0
    else:
        return int(n % 10) + sum_positive(int(n//10))


print(sum_positive(1234))
