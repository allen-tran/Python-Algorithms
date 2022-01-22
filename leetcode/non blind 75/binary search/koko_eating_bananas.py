'''
https://leetcode.com/problems/koko-eating-bananas/
'''


from math import ceil


def minEatingSpeed(piles, h):
    def solve(k):
        c = h
        for p in piles:
            c -= int(ceil(p/k))
        return c >= 0
    l = 1
    r = max(piles)
    while l <= r:
        mid = (l+r)//2
        if solve(mid):
            r = mid - 1
        else:
            l = mid + 1
    return l
