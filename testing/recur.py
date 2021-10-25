'''

'''

def re(n, m):
    if (n > 0):
        return re(n-1, m + n)
    else:
        return m

print(re(3, 0))