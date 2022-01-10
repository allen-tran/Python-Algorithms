"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
"""


def minRemoveToMakeValid(s):
    parenthese = []
    invalid_index = []
    for i, c in enumerate(s):
        if c == "(":
            parenthese.append(c)
            invalid_index.append(i)
        if c == ")":
            if len(parenthese) == 0:
                invalid_index.append(i)
            else:
                parenthese.pop()
                invalid_index.pop()
    res = ""
    for j in range(len(s)):
        if j not in invalid_index:
            res += s[j]
    return res
