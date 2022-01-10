"""
https://leetcode.com/problems/3sum-smaller/
"""


class Solution:
    def threeSumSmaller(self, nums, target):
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            count += self.search_pair(nums, target - nums[i], i)
        return count

    def search_pair(self, arr, target_sum, first):
        count = 0
        left, right = first + 1, len(arr) - 1

        while left < right:
            if arr[left] + arr[right] < target_sum:
                count += right - left
                left += 1
            else:
                right -= 1
        return count
