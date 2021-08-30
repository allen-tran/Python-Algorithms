'''
#49 medium
Time: O(nlogn * m)
'''

def group(strs):
    # key: sorted word, value: LISTS of original words
    dict = {}
    # loop through all of the words in strs
    for word in strs:
        # get the sorted words by doing sorted(word) and joining it to any empty string to convert it to string
        sortedword = "".join(sorted(word))
        # if we have not see this sortedword before we must add it to the dictionary in a new list
        if sortedword not in dict:
            dict[sortedword] = [word]
        else:
            # else add it to the dictionary of the list by appending it
            dict[sortedword].append(word)
    # list we will store the lists in
    result = []
    # for each of the items in the dictionary values, append it to the result list
    for item in dict.values():
        result.append(item)
    # return the list of lists
    return result