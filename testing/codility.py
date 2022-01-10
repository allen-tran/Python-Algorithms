def ways(total, k):
    sum = {}
    m = 1000000007

    i = 1
    if total < 0:
        return 0
    elif total == 0:
        return 1
    elif k < 1:
        return 0
    else:
        key = (total, i, k)
        if key not in sum:
            # better approach to return integer modulo
            sum[key] = (ways(total - k, k) + ways(total, k - 1)) % m
        return sum[key]


# take input totak and k


print(ways(8, 2))
