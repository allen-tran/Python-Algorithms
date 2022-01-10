"""
https://leetcode.com/problems/delete-node-in-a-linked-list/
"""


def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next
