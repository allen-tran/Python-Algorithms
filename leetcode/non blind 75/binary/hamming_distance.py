'''
https://leetcode.com/problems/hamming-distance/submissions/
'''


def hammingDistance(x, y):
    return bin(x ^ y).count('1')
