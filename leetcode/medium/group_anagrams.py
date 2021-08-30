'''
#49 medium
Time: O(nlogn * m)
'''

def group(strs):
    # key: sorted word, value: LISTS of original word
    dict = {}
    for word in strs:
        sortedword = "".join(sorted(word))
        if sortedword not in dict:
            dict[sortedword] = [word]
        else:
            dict[sortedword].append(word)
    result = []

    for item in dict.values():
        result.append(item)
    return result