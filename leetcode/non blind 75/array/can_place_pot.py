"""
https://leetcode.com/problems/can-place-flowers/
"""


def canPlaceFlowers(flowerbed, n):
    new_bed = [0] + flowerbed + [0]

    for i in range(1, len(new_bed) - 1):
        if new_bed[i] == 0 and new_bed[i - 1] == 0 and new_bed[i + 1] == 0:
            n -= 1
            new_bed[i] = 1

    if n <= 0:
        return True

    return False
