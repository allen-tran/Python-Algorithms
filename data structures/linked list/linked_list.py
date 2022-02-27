class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add(self, value) -> None:
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        
    def remove(self, value) -> None:
        if not self.head:
            print('Linked list empty!')
            return
        curr = self.head
        prev = None
        while curr:
            if curr.val == value:
                if prev and curr.next:
                    prev.next = curr.next
                elif not prev and curr.next:
                    self.head = self.head.next
                elif not prev and not curr.next:
                    self.head = None
            prev = curr
            curr = curr.next

    def get_values(self):
        curr = self.head
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next

        return res
ll = LinkedList()
ll.add(5)
print(ll.get_values())
ll.add(3)
print(ll.get_values())
ll.remove(3)
print(ll.get_values())
ll.remove(3)
print(ll.get_values())
ll.remove(5)
print(ll.get_values())


