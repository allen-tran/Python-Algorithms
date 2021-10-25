'''
https://leetcode.com/problems/implement-strstr/
'''


def strStr(self, haystack: str, needle: str) -> int:
    if not needle:
        return 0

    for i in range(0, len(haystack)):
        temp = str(haystack[i:len(needle)+i])
        if temp == needle:
            return i
    return -1
