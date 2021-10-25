'''
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
'''

def findDisappearedNumbers(nums):
    return list(set(range(1, len(nums) + 1)) - set(nums))