'''
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
'''


def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
    max_len, start = 0, 0
    frequency = {}

    for end in range(len(s)):
        right = s[end]
        if right not in frequency:
            frequency[right] = 0
        frequency[right] += 1

        while len(frequency) > 2:
            left = s[start]
            frequency[left] -= 1
            if frequency[left] == 0:
                del frequency[left]
            start += 1
        max_len = max(max_len, end-start+1)

    return max_len
