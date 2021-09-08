'''
#448 easy
'''

def findDisappearedNumbers(nums):
    return list(set(range(1, len(nums) + 1)) - set(nums))