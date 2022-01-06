"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""


def reverseWords(s):
    res_s = ""
    new_s = s.split(" ")
    for i in range(len(new_s)):
        res_s += new_s[i][::-1]
        if i != len(new_s) - 1:
            res_s += " "
    return str(res_s)
