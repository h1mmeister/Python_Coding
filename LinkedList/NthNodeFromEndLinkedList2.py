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
        first = self.head
        second = self.head
        if self.head is None:
            return
        count = 0
        while count < n:
            if second is None:
                print("You can't check the node!!")
                return
            second = second.next
            count += 1
        while second:
            first = first.next
            second = second.next
        print(first.data)


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(35)
llist.nth_node_from_end_of_linked_list(5)