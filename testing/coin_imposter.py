def comparison(n):
    if n == 1:
        return n
    print(n)
    return comparison(n//2)


print(comparison(90))
