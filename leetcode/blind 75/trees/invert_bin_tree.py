'''
https://leetcode.com/problems/invert-binary-tree/
'''

from collections import deque


def invertTree(root):
    if not root:
        return None

    q = deque()
    q.append(root)

    while(q):
        rem = q.popleft()
        rem.left, rem.right = rem.right, rem.left
        if (rem.left):
            q.append(rem.left)
        if (rem.right):
            q.append(rem.right)

    return root
