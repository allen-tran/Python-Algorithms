"""
https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
"""


def minimumDifference(nums, k):
    nums.sort()

    l, r = 0, k - 1

    min_diff = float("inf")

    while r < len(nums):
        min_diff = min(min_diff, nums[r] - nums[l])

        l, r = l + 1, r + 1
    return min_diff
