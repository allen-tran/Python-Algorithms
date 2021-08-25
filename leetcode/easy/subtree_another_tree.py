'''
#572 easy (should be medium imo)
'''
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root, subRoot):
    if root == None:
        return False
    elif isSubEqual(root, subRoot):
        return True
    else:
        return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

        
def isSubEqual(s, t):
    if s == None or t == None:
        return s == None and t == None
    elif s.val == t.val:
        return isSubEqual(s.left, t.left) and isSubEqual(s.right, t. right)
    else:
        return False