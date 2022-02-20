"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""


def maxProfit(prices):
    # iterate throgh the for loop
    # only concern is how to know whne to buy it again and sell it
    i = 0
    result = 0

    while i < len(prices) - 1:
        curr = i + 1
        if prices[curr] - prices[i] > 0:
            result += prices[curr] - prices[i]
        i = curr

    return result
