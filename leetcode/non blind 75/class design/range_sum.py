'''
https://leetcode.com/problems/range-sum-query-immutable/
'''


class NumArray:
    dict = {}

    def __init__(self, nums):

        self.dict[0] = nums[0]
        for i in range(1, len(nums)):
            self.dict[i] = self.dict[i-1] + nums[i]

    def sumRange(self, left: int, right: int):
        if left == 0:
            return self.dict[right]
        else:
            return (self.dict[right] - self.dict[left-1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
