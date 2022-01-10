"""
https://leetcode.com/problems/subarray-product-less-than-k/
"""


def numSubarrayProductLessThanK(nums, k):
    left, count, prod = 0, 0, 1

    for right in range(len(nums)):
        prod *= nums[right]

        while prod >= k and left <= right:
            prod /= nums[left]
            left += 1

        count += right - left + 1

    return count
