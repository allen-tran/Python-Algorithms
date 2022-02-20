"""
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.
"""


def remove_duplicates(arr):
    next_non_dup = 0

    i = 0

    while i < len(arr):
        if arr[i] != arr[next_non_dup - 1]:
            arr[next_non_dup] = arr[i]
            next_non_dup += 1
        i += 1
    return next_non_dup
