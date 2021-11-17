'''
https://leetcode.com/problems/unique-paths/
'''


def uniquePaths(m, n):
    d = [[1] * n for _ in range(m)]
        for col in range(1, m):
            for row in range(1, n):
                d[col][row] = d[col-1][row] + d[col][row-1]
    return d[m-1][n-1]
