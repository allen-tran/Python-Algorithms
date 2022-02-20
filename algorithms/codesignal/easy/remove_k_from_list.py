 class ListNode(object):
    def __init__(self, x):
        value = x
        next = None

def removeKFromList(l, k):
    # create dummy node with no value
    dummy = ListNode(None)
    # dummy's next pointer is directed toward the head
    dummy.next = l

    # we start the current at dummy
    curr = dummy
    
    # while current is not None
    while curr:
        # while current's point is not none and the next node is the target
        while curr.next and curr.next.value == k:
            # the current pointer will be pointed to the next next node, deleting the next node
            curr.next = curr.next.next
        # we can advance current
        curr = curr.next
    # return the linked list now
    return dummy.next