'''
#70 easy
'''

def climb(n):
    if n <= 2:
        return n
    else:
        a, b = 1, 2
        for i in range(n-2):
            c = a + b
            a = b
            b = c
    return b

print(climb(5))