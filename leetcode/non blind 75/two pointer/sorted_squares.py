"""
https://leetcode.com/problems/squares-of-a-sorted-array/
"""


def sortedSquares(nums):
    """
    naive: O(n+nlogn)
    """
    res = []
    for i in nums:
        res.append(i * i)

    res.sort()
    return res

    """    
    two pointers left and right
    compare the absolute values
    optimal: O(n)
    """
    n = len(nums)

    result = [0] * n
    l, r = 0, n - 1

    for i in range(n - 1, -1, -1):
        if abs(nums[l]) < abs(nums[r]):
            square = nums[r]
            r -= 1
        else:
            square = nums[l]
            l += 1
        result[i] = square * square

    return result
