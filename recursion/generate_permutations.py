'''
methods to generate permuatations of a list
'''

def permutate(nums):
    if not nums:
        return []
    elif len(nums) == 1:
        return [nums]
    res = []

    for i in range(len(nums)):
        m = nums[i]
        remList = nums[:i] + nums[i+1:]
        for p in permutate(remList):
            res.append([m] + p)
    return res

print(permutate([1,2,3,4,5]))