"""
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""


def preorderTraversal(root):
    if not root:
        return []

    stack = [root]
    ret = []

    while stack:
        tmp = stack.pop()
        if tmp:
            ret.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
    return ret
