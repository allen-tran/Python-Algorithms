"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
"""


def pair_with_target_sum(arr, target_sum):
    left, right = 0, len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target_sum:
            return [left, right]
        if curr_sum < target_sum:
            left += 1
        if curr_sum > target_sum:
            right -= 1
    return [-1, -1]


if __name__ == "__main__":
    print(pair_with_target_sum([1, 2, 3, 4, 5], 9))
