'''
https://leetcode.com/problems/subarray-sum-equals-k/
'''


def subarraySum(nums, k):
    prevMap = {0: 1}
    count = 0
    s = 0

    for num in nums:
        s += num
        if s-k in prevMap:
            count += prevMap-[s-k]
        if s in prevMap:
            prevMap[s] += 1
        else:
            prevMap[s] = 1
    return count
