'''
#206 easy
'''

def reverse(head):
    prev = None
    
    # while head is not null
    while (head):
        # create a temperary variable and assign it as head's value
        temp = head
        # advance head to next
        head = head.next
        # the next val after head is previous
        temp.next = prev
        # assign to previous
        prev = temp
    # return previous to have it reversed       
    return prev

'''
Alternate way to do it
'''

def reverse(head):
    prev = None
    curr = head
    nextN = None

    # while current is not None
    while curr:
        # assign the next node to be the node after current
        nextN = curr.next
        # switch the arrow from current to be pointed towards previous
        curr.next = prev
        # advance previous
        prev = curr
        # update current to the be the next node
        curr = nextN
    # return previous to have it reversed
    return prev