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
        temp = self.head
        if n == length:
            self.head = temp.next
            temp = None
            return
        temp = self.head
        for i in range(1, length - n):
            temp = temp.next
        if temp is None:
            return
        temp.next = temp.next.next

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next


llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.push(0)
llist.printList()
llist.nth_node_from_end_of_linked_list(10)
print("\n")
llist.printList()