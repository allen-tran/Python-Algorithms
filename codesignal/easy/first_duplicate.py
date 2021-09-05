def firstDuplicate(a):
    # dictionary that will keep track of the value and the indicies
    seenDict = {}
    
    for i, j in enumerate(a):
        
        if j not in seenDict:
            seenDict[j] = [i]
        else:
            seenDict[j].append(i)
        if len(seenDict[j]) == 2:
            return j
        
    return -1