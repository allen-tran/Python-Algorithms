'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    if not head:
        return []
    dummy = ListNode(None)
    dummy.next = head
    slow = dummy
    fast = dummy
    
    for i in range(n+1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dummy.next