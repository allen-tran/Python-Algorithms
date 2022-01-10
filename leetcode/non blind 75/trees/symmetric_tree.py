"""
https://leetcode.com/problems/symmetric-tree/
"""


class Solution:
    def isSymmetric(self, root):
        if root is None:
            return
        return self.isMirror(root, root)

    def isMirror(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        else:
            return (
                left.val == right.val
                and self.isMirror(left.left, right.right)
                and self.isMirror(left.right, right.left)
            )
