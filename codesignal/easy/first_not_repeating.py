def firstNotRepeatingCharacter(s):
    # key: character, value: indices 
    dict = {}
    for i in range(len(s)):
        # if its not in the dictionary, create a list for it
        if s[i] not in dict:
            dict[s[i]] = [i]
        else:
            # if it is in the dictionary, append the index of it
            dict[s[i]].append(i)
    # loop through and check if there are less than two indicies
    for i in dict:
        # if there is, we can return the key
        if  len(dict[i]) < 2:
            return i
    # if not, return '_'
    return '_'