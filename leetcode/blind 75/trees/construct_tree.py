"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    # base case for recursion
    if not preorder or not inorder:
        return None
    # create a node based on the first val of preorder list
    # this will be the root of the tree
    root = TreeNode(preorder[0])

    # find where the root node exists in the inorder list
    # set it to the middle
    mid = inorder.index(preorder[0])

    # work on the left subtree now
    # we will shrink the preorder list to go from the next node to the mid node
    # then we will shrink the inorder list to only the left half of nodes
    root.left = buildTree(preorder[1 : mid + 1], inorder[:mid])

    # call everything above again. assign new node as the root (20)
    # since we are on the right side we care about the right side of the preorder
    # and we care about the right side of the inorder as well
    root.right = buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

    # return root when we are done because we have been assigning left and right
    return root


print(buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
