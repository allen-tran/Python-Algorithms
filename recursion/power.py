'''
Calculate the power of a number using recursion
'''


def power(num, p):
    assert int(
        p) == p and p >= 0, 'The exponent must be positive a positive integer.'

    if p == 0:
        return 1
    elif p == 1:
        return num
    else:
        return num * power(num, p-1)


print(power(6, 4))
