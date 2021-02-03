

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""


# This function should rotate list counter-
# clockwise by k and return head node
def rotate(head, k):
    # code here
    if k == 0:
        return
    temp = head
    while k > 1 and temp:
        temp = temp.next
        k -= 1
    if temp is None:
        return
    kth_node = temp
    while temp.next:
        temp = temp.next
    temp.next = head
    head = kth_node.next
    kth_node.next = None
    return head
