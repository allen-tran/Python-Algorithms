'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
'''

from collections import deque


def levelOrder(root):
    if not root:
        return None

    q = deque()
    q.append(root)
    res = []
    while q:
        new_list = []
        qsize = len(q)
        for i in range(qsize):
            rem = q.popleft()
            if rem.left:
                q.append(rem.left)

            if rem.right:
                q.append(rem.right)
            new_list.append(rem.val)
        res.append(new_list)

    return res
