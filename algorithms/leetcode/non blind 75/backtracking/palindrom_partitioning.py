"""
https://leetcode.com/problems/palindrome-partitioning/
"""


def partition(self, s: str) -> List[List[str]]:
    def isPalindrome(start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def dfs(start, path):
        if start >= len(s):
            self.res.append(path)
        for l in range(len(s) - start):
            if isPalindrome(start, start + l):
                dfs(start + l + 1, path + [s[start : start + l + 1]])

    self.res = []
    dfs(0, [])
    return self.res
