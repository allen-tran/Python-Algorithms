'''
#53 easy
'''
# LINEAR
def maxSubArray(nums) -> int:
    maxSub = nums[0] # take the first index, this will take care of a list with just one number
    currSum = 0 # this will update with the sums and have the largest at the end

    for n in nums:
        if currSum < 0: 
            currSum = 0 # we will never take the leading negative numbers
        currSum += n
        maxSub = max(maxSub, currSum)
    return maxSub

print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))