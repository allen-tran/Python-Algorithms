def qaly():
    years = int(input())
    total = 0
    for i in range(years):
        q, p = [float(x) for x in input().split()]
        total += q * p

    print(total)


qaly()
