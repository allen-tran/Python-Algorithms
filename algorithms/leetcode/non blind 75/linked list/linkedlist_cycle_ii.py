"""
https://leetcode.com/problems/linked-list-cycle-ii/
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersect(self, head):
        slow, fast = head, head

        if head is None:
            return None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return slow

        return None

    def detectCycle(self, head):
        if head is None:
            return None
        intersect = self.getIntersect(head)
        if intersect is None:
            return None

        p1 = head
        p2 = intersect

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1
