"""
https://leetcode.com/problems/longest-common-prefix/submissions/
"""


def longestCommonPrefix(strs):
    strs.sort(key=len)
    res = strs[0]
    for s in strs:
        while res != s[0 : len(res)]:
            res = res[:-1]
    return res
