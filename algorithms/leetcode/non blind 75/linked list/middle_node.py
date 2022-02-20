"""
https://leetcode.com/problems/middle-of-the-linked-list/submissions/
"""


def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
