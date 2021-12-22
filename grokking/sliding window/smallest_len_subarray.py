'''
Given an array of positive numbers and a positive number S, find the length of the smallest contiguous subarray whose sum is greater than or equal to S. Return 0 if no such subarray exists.
'''


def smallest_subarray_with_given_sum(s, arr):
  window_sum = 0
  start = 0
  min_len = float('inf')

  for end in range(len(arr)):
    window_sum += arr[end]

    while window_sum >= s:
      min_len = min(min_len, end-start+1)
      window_sum -= arr[start]
      start += 1
  return min_len if (min_len != float('inf')) else 0
