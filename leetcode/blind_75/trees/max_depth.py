import collections
from collections import deque

# breadth first search
def maxDepth(root):
    if not root:
        return 0
    count = 0
    q = collections.deque()
    q.append(root)

    while q:
        qsize = len(q)
        count+=1
        for i in range(qsize):
            rem = q.popleft()
            if rem.left:
                q.append(rem.left)
            if rem.right:
                q.append(rem.right)
    return count

'''
depth first search
def maxDepth(root):
    if not root:
        return 0
    count = max(self.maxDepth(root.left), self.maxDepth(root.right))+1
    
    return count
'''