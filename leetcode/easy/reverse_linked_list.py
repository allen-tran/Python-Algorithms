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
        # assign to 
        prev = temp
            
    return prev

'''
Alternate way to do it
'''

def reverse(head):
    prev = None
    curr = head
    nextN = None

    while (curr is not None):
        