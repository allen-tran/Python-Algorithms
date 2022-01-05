"""
https://leetcode.com/problems/sort-colors/
"""


def sortColors(nums):
    left, right = 0, len(nums) - 1
    i = 0

    while i <= right:
        if nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
            i += 1
        elif nums[i] == 1:
            i += 1
        else:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1

    return nums
