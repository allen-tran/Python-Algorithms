'''
https://leetcode.com/problems/climbing-stairs/
O(n)
'''


def climb(n):
    # the first two stairs will only have either one or two distinct ways to get up
    if n <= 2:
        # just return whatever n is if its 2 or less
        return n
    else:
        # if not, we have a be 1 and b be the second way to get up
        a, b = 1, 2
        # we dont go all the way up because the first two are already taken care of
        for i in range(n-2):
            # first add the two numbers together
            c = a + b
            # then we shift to the right. make a the second largest number
            a = b
            # make b the largest number (newest number)
            b = c
    # we return b because it will always be the right most, greatsest number
    return b


print(climb(5))
