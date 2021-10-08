def productExceptSelf(nums):
    #create resultant list
    res = []
    # initialize pre and post fix lists within value 1 to start off the multiplying
    prefix = [1]
    postfix = [1]

    # multiply the number in prefix with the numbers    
    for i in range(len(nums)):
        prefix.append(prefix[i]* nums[i])
        
    # mutliply going down the lists
    for i in range(len(nums)):
        postfix.insert(0, (postfix[i-(i+i+1)] * nums[i-(i+i+1)]))
            
    for i in range(len(nums)):
        res.append(prefix[i] * postfix[i+1])
            
    return res