'''
https://leetcode.com/problems/contains-duplicate/
'''


def containsDuplicate(self, nums: List[int]) -> bool:
    dict = {}

    for i in range(len(nums)):
        if nums[i] not in dict:
            dict[nums[i]] = [i]
        else:
            dict[nums[i]].append(i)
        if len(dict[nums[i]]) >= 2:
            return True

    return False
