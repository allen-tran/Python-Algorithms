"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
"""


def removeDuplicates(nums):
    # start with a the next number after first
    len_ = 1
    # trivial case
    if len(nums) == 0:
        return 0
    # starting with the second number go through
    for i in range(1, len(nums)):
        # check if the number before is NOT equal to what we are looking at
        if nums[i] != nums[i - 1]:
            # if not equal we found a good number and we can set it to that
            nums[len_] = nums[i]
            # increase our worker
            len_ += 1
    # return where the work is. this how long our non duplicated array is
    return len_
