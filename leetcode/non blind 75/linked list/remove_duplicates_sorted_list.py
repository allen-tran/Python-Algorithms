'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Time: O(n)
'''


def deleteDuplicates(head):
    prevMap = {}
    curr = head

    while curr:
        while curr.next and curr.next.val == curr.val:
            curr.next = curr.next.next
        curr = curr.next
    return head
