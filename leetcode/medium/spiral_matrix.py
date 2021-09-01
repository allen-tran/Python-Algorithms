'''
#54 medium
'''

def spiral(matrix):
    if not matrix:
        return []
    
    rowbegin = 0
    rowend = len(matrix)
    columnbegin = 0
    columnend = len(matrix)
    