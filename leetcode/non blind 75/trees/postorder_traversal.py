"""
https://leetcode.com/problems/binary-tree-postorder-traversal/
"""


def postorderTraversal(root):
    if not root:
        return
    stack, res = [root], []

    while stack:
        tmp = stack.pop()
        if tmp:
            res.append(tmp.val)
            if tmp.left:
                stack.append(tmp.left)
            if tmp.right:
                stack.append(tmp.right)

    return res[::-1]
