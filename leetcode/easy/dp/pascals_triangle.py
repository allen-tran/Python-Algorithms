'''
https://leetcode.com/problems/pascals-triangle/
'''


def generate(self, numRows: int):
    # create first list within the list
    res = [[1]]

    # iterate through only n-1 because we already made the first row
    for i in range(numRows - 1):
        # add zeros to both side to add
        temp = [0] + res[-1] + [0]
        # create row to store new added values in
        row = []
        # iterate through up until the longest row + 1 because we gotta add a new number
        for j in range(len(res[-1])+1):
            # add to the row with the numbers added
            row.append(temp[j] + temp[j+1])
        # add the rows to the res
        res.append(row)
    return res
