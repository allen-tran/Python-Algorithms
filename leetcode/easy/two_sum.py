'''
#1 easy
'''
# BRUTE FORCE
def twoSum(nums, target: int):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return

print(twoSum([2,6,3,5,8], 5))

# HASH MAP
