'''
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.
'''


def length_of_longest_substring(arr, k):
    # TODO: Write your code here
    start, max_len, max_ones = 0, 0, 0
    freq_map = {}

    for end in range(len(arr)):
        right = arr[end]
        if right not in freq_map:
            freq_map[right] = 0
        freq_map[right] += 1

        max_ones = max(max_ones, freq_map[right])
        if (end-start + 1) - max_ones > k:
            left = arr[start]
            freq_map[left] -= 1
            start += 1
        max_len = max(max_len, end-start + 1)
    return max_len
