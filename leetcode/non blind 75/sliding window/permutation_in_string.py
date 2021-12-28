"""
https://leetcode.com/problems/permutation-in-string/submissions/
"""


def checkInclusion(self, s1: str, s2: str) -> bool:
    start, matched = 0, 0
    char_freq = {}

    for char in s1:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1

    for end in range(len(s2)):
        right = s2[end]
        if right in char_freq:
            char_freq[right] -= 1

            if char_freq[right] == 0:
                matched += 1

        if matched == len(char_freq):
            return True

        if end >= len(s1) - 1:
            left = s2[start]
            start += 1
            if left in char_freq:
                if char_freq[left] == 0:
                    matched -= 1
                char_freq[left] += 1
