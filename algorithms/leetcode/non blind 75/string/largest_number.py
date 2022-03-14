from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        for index, value in enumerate(nums):
            nums[index] = str(value)

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare))

        return str(int("".join(nums)))
