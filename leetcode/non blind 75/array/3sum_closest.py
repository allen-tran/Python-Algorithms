'''
https://leetcode.com/problems/3sum-closest/
'''

import math


def threeSumClosest(nums, target):
    smallest = math.inf
    nums.sort()

    for i in range(len(nums)-2):
        left, right = i + 1, len(nums)-1
        while left < right:
            target_diff = target - (nums[i] + nums[left] + nums[right])

            if target_diff == 0:
                return target

            if abs(target_diff) < abs(smallest) or (abs(target_diff) == abs(smallest) and target_diff > smallest):
                smallest = target_diff
            if target_diff > 0:
                left += 1
            else:
                right -= 1
    return target - smallest
