'''
Find the greatest common divisor of two numbers using recursion
Ex. gcd(8, 12) = 4
8  = 2*2*2
12 = 2*2*3
gcd(a, 0) = a
gcd(a, b) = gcd(b, a mod b)
'''


def gcd(a, b):
    assert int(a) == a and int(b) == b, 'Numbers must be integers.'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(16, 4))
