class TreeNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution:
    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append('N')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialzie(self, data):
        values = data.split(',')
        self.i = 0

        def dfs():
            if values[self.i] == 'N':
                self.i+=1
                return None
            node = TreeNode(int(values[self.i]))
            self.i += 1 
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()