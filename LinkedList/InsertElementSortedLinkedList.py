# Given a sorted linked list and a value to insert, write a function to insert the value in a sorted way.

def sortedInsert(head1, key):
    # code here
    # return head of edited linked list
    if head1 is None:
        new_node = Node(key)
        head1 = new_node

    elif head1.data >= key:
        new_node = Node(key)
        new_node.next = head1
        head1 = new_node
    else:
        temp = head1
        prev = None
        while temp and temp.data < key:
            prev = temp
            temp = temp.next

        new_node = Node(key)
        new_node.next = prev.next
        prev.next = new_node

    return head1
