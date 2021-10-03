def inorderTraversal(root):
        if not root:
            return []
        return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)