def reverse(head):
    current = head
    prev = None
    while current:
        other = current.next
        current.next = prev
        prev = current
        current = other
    return prev


def addOne(head):
    # Returns new head of linked List.
    head = reverse(head)
    carry = 0
    temp = head
    prev = None
    head.data += 1

    while temp and (temp.data > 9 or carry > 0):
        temp.data += carry
        carry = temp.data // 10
        temp.data %= 10
        prev = temp
        temp = temp.next

    if carry > 0:
        prev.next = Node(carry)

    return reverse(head)