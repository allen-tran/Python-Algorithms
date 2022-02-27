from platform import node


class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class QueueStack:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def add(self, number):
        temp = Node(number)
        if not self.head:
            self.head = temp
            self.tail = node
        else:
            self.tail.next = None
            self.tail = node
        self._size += 1

    def pop(self):
        if self._size == 0:
            print('Stack Empty!')
            return
        curr = self.head
        while curr != self.tail:
            curr = curr.next
        tail_val = self.tail.val
        self.tail = curr
        self._size -= 1
        return tail_val

    def __len__(self):
        return self._size

if __name__ == '__main__':
    q = QueueStack()
    q.add(5)
    q.pop()