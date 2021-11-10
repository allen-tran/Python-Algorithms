'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''


def lengthOfLongestSubstring(s):
    # create new set
    newSet = set()
    # create left point
    l = 0
    # resultant length
    res = 0

    # loop through string with right pointer as iterator
    for r in range(len(s)):
        # if we found a repeating chracter
        while s[r] in newSet:
            # remove the first occurance
            newSet.remove(s[l])
            # advance left pointer
            l += 1
        # add the new chacter to set no matter what
        newSet.add(s[r])
        # find out the max by comparing the right pointer minus the left pointer
        # but plus 1 to get the true lenghth of the substring
        res = max(res, (r - l) + 1)

    return res
