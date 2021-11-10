'''
https://leetcode.com/problems/set-matrix-zeroes/
'''


def setZeroes(matrix):

    zeroCol = [False for i in range(len(matrix[0]))]
    zeroRow = [False for i in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zeroCol[j] = True
                zeroRow[i] = True

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if zeroCol[j] == True or zeroRow[i] == True:
                matrix[i][j] = 0
