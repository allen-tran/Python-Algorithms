class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class BinaryTree:
    def __init__(self):
        self.root = None
        self._size = 0
        
    def add(self, node):
        if self.size == 0:
            self.root = node
        
    def remove(self, node):
        pass
    
    @property
    def size(self):
        return self._size
    