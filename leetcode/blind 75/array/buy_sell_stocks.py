'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''


def buy_sell(prices):
    # create pointers to the stock prices
    l, r = 0, 1
    # create max variable to compare to
    maxP = 0

    # while right pointer doesn't reach out of bounds
    while r < len(prices):
        # left value should never be greater than the right value because we only want profits
        if prices[l] < prices[r]:
            # compare the profit
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            # if we found a value smaller than left, we want to update left to that value
            l = r
        # keep incrementing no matter what
        r += 1

    return maxP
