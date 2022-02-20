"""
Given an unsorted array of numbers and a target key, remove all instances of key in-place and return the new length of the array.
"""


def remove_element(arr, key):
    next_elem = 0

    for i in range(len(arr)):
        if arr[i] != key:
            arr[next_elem] = arr[i]
            next_elem += 1
        return next_elem
