def triangle(nums):
    res = []
    for i in range(0, len(nums)-2):
        if (nums[i] + nums[i+1] > nums[i+2]) and (nums[i] + nums[i+2] > nums[i+1]) and (nums[i+1] + nums[i+2] > nums[i]):
            res.append(1)
        else:
            res.append(0)
    return res


print(triangle([1, 2, 2, 4]))
