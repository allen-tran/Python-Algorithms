'''
#54 medium
Time Complexity: O(m*n)
Space Complexity: O(1)
'''

def spiral(matrix):
    if not matrix:
        return []
    
    res = [] # result
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    while left < right and top < bottom:
        # get every value in the top row
        for i in range(left, right): # from 0-2 (3)
            res.append(matrix[top][i])
        top += 1 # it will shift top bound by 1

        # get every i in the right col
        for j in range(top, bottom):
            res.append(matrix[j][right - 1])
        right -= 1 # it will shift right bound over to the left by 1

        # this is a double check to account the edge cases where the matrix is either straight vertically or straight horizontally
        if not (left < right and top < bottom):
            break

        # get every i in the bottom row
        for k in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][k])
        bottom -= 1 # it will shift bottom bound up to by 1

        # get every i in the left column
        for l in range(bottom - 1, top -1, -1):
            res.append(matrix[l][left])
        left += 1
    
    return res
        
print(spiral([[1,2,3], [4, 5, 6], [7, 8, 9]]))
    