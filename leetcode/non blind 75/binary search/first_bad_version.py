"""
https://leetcode.com/problems/first-bad-version/
"""


def firstBadVersion(n):
    l, r = 1, n

    while l < r:
        mid = (r - l) // 2 + l
        if not isBadVersion(mid):
            l = mid + 1
        else:
            r = mid
    return l
