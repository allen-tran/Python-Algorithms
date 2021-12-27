'''
Given a string with lowercase letters only, if you are allowed to replace no more than k letters with any letter, find the length of the longest substring having the same letters after replacement.
'''


def length_of_longest_substring(str, k):
    max_len, start, max_repeat_char_count = 0, 0, 0
    char_freq = {}

    for end in range(len(str)):
        right = str[end]
        if right not in char_freq:
            char_freq[right] = 0
        char_freq[right] += 1

        max_repeat_char_count = max(max_repeat_char_count, char_freq[right])

        if ((end-start+1) - max_repeat_char_count > k):
            left = str[start]
            char_freq[left] -= 1
            start += 1

        max_len = max(max_len, end-start+1)

    return max_len
