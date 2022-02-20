class LinkedNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, val):
        node = LinkedNode(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def popleft(self):
        if self.size == 0:
            return
        value = self.head.val
        self.head = self.head.next
        self.size -= 1
        
        return value

    def __len__(self):
        return self.size