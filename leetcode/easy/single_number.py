'''
#136 easy
'''

def single(nums):
    dict = {}
    for i in range(len(nums)):
        if nums[i] not in dict:
            dict[nums[i]] = [i]
        else:
            dict[nums[i]].append(i)
                
    for i in dict:
        if len(dict[i]) < 2:
            return i

print(single([1,2,3,54,3,2,1,24,5,4]))