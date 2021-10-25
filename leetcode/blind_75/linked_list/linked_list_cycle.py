'''
https://leetcode.com/problems/linked-list-cycle/
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: ListNode):

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True

    return False
