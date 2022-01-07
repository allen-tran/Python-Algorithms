"""
https://leetcode.com/problems/next-permutation/
"""


def next_permutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i = j = len(nums) - 1

    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1

    if i == 0:
        nums.reverse()
        return

    while nums[i - 1] >= nums[j]:
        j -= 1

    nums[j], nums[i - 1] = nums[i - 1], nums[j]

    nums[i:] = nums[len(nums) - 1 : i - 1 : -1]
