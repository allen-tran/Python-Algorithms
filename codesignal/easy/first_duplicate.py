def firstDuplicate(a):
    # dictionary that will keep track of the value and the indicies
    seenDict = {}

    # i is the index, j is the value
    for i, j in enumerate(a):
        # if we have not seen it yet, create a list of the indices
        if j not in seenDict:
            seenDict[j] = [i]
        else:
            # if we seen it, just append the index to the list
            seenDict[j].append(i)

        # as we move through the list, if we have dupliates, return the first duplicated number
        if len(seenDict[j]) == 2:
            return j
    # return -1 if there are no duplicates
    return -1
