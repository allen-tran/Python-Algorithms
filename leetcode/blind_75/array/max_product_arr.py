def maxProduct(nums):
    res = max(nums)
    currMax, currMin = 1, 1

    for i in nums:
        if i == 1:
            currMax, currMin = 1, 1
            continue
        temp = currMax * i
        currMax(i*currMax, i*currMin, i)
        currMin(temp, i*currMin, i)
        res = max(res, currMax)
    return res
