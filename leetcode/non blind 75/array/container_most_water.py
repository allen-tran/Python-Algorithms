"""
https://leetcode.com/problems/container-with-most-water/
"""


def maxArea(height):
    l, r = 0, len(height) - 1
    currArea = 0
    while l < r:
        newArea = (r - l) * min(height[l], height[r])
        currArea = max(currArea, newArea)
        if height[l] < height[r]:
            l += 1
        elif height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return currArea
