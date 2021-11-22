class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder):
        self.postorder = postorder
        self.idx_map = {idx: val for val, idx in enumerate(inorder)}
        return self.helper(0, len(inorder)-1)

    def helper(self, in_left, in_right):

        if in_left > in_right:
            return None
        val = self.postorder.pop()
        root = TreeNode(val)
        index = self.idx_map[val]

        root.right = self.helper(index+1, in_right)
        root.left = self.helper(in_left, index-1)

        return root
