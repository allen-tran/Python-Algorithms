'''
https://leetcode.com/problems/find-bottom-left-tree-value/
'''

from queue import deque


def findBottomLeftValue(root):
    q = deque([root])

    while q:
        node = q.popleft()
        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)
    return node.val
