"""
Write a function to return the maximum number of fruits in both baskets.
"""


def fruits_into_baskets(fruits):
    # TODO: Write your code here
    max_length, start = 0, 0
    fruit_frequency = {}

    for end in range(len(fruits)):
        right = fruits[end]
        if right not in fruit_frequency:
            fruit_frequency[right] = 0
        fruit_frequency[right] += 1

        while len(fruit_frequency) > 2:
            left = fruits[start]
            fruit_frequency[left] -= 1
            if fruit_frequency[left] == 0:
                del fruit_frequency[left]
            start += 1
        max_length = max(max_length, end - start + 1)
    return max_length
