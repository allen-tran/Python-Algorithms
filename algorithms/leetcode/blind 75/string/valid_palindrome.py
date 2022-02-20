'''
https://leetcode.com/problems/valid-palindrome/
'''


def isPalindrome(s):
    res = []
    for i in s:
        if i.isalpha() or i.isnumeric():
            res.append(i.lower())
    if res == res[::-1]:
        return True
    else:
        return False
