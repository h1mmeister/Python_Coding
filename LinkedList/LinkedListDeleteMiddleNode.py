"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
"""


def deleteMid(head):
    """
    head:  head of given linkedList
    return: head of resultant llist
    """

    # code here
    if head is None or head.next is None:
        return None

    slow = fast = head
    prev = None

    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    prev.next = slow.next
    return head
