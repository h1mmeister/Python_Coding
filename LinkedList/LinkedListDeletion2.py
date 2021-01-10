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

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def delete_node(self, pos):
        temp = self.head
        prev = None
        if temp is None:
            return
        if pos == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(0, pos):
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None



llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)

print("Created Linked List: ")
llist.printList()
llist.delete_node(4)
print("\nLinked List after Deletion of 1:")
llist.printList()
