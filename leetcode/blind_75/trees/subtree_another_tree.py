'''
#572 easy (should be medium imo)
'''
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root, subRoot):
    # tivial case if there is not root we can return false
    if root == None:
        return False
    # this will take care of the case where the whole s tree is equal to the t tree
    elif isSubEqual(root, subRoot):
        return True
    # this is where the real check is to see if there exists the subroot
    else:
        # recursively either goes down the left side or right side
        return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

        
def isSubEqual(s, t):
    # makes sure that if one of them are empty, both are empty
    if s == None or t == None:
        return s == None and t == None
    # we move on to next case where if one of the values are equal
    elif s.val == t.val:
        # we recursively move down the left side to keep checking and the right side to keep checking
        return isSubEqual(s.left, t.left) and isSubEqual(s.right, t. right)
    # if it doesn't pass we return false
    else:
        return False