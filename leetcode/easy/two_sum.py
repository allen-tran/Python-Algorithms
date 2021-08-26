'''
#1 easy
'''
# BRUTE FORCE
'''
def twoSum(nums, target: int):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return

print(twoSum([2,6,3,5,8], 5))

'''

# HASH MAP aka One Pass
# Time: O(n)
# Space: O(n)

def twoSum(nums, target):
    # every previous element we visit will be stored in here
    # value : index
    prevMap = {}
    # i id index and value is n 
    for i, n in enumerate(nums):
        # we need to first check to see if the difference is already in the hashmap or not
        diff = target - n
        #  if it is, we can return the indices first of the difference index and the current element index
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return