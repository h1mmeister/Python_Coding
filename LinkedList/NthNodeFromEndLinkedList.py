class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def nth_node_from_end_of_linked_list(self, n):
        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.next
        print(length)
        if n > length:
            return
        temp = self.head
        for i in range(0, length - n):
            temp = temp.next
        print(temp.data)


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(35)
llist.nth_node_from_end_of_linked_list(4)