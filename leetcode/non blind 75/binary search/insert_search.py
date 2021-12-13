'''
https://leetcode.com/problems/search-insert-position/submissions/
'''


def searchInsert(nums, target):
    l, r = 0, len(nums)-1
    mid = float('inf')
    while l <= r:
        mid = (r - l) // 2 + l

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
    return l
