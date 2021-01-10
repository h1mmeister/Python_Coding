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
            print(temp.data, end=' ')
            temp = temp.next

    def detect_loop2(self):
        main = self.head
        ref = self.head
        while ref and main and main.next:
            main = main.next.next
            ref = ref.next
            if ref == main:
                return True
        return False




llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

#llist.head.next.next.next.next = llist.head;

if llist.detect_loop2():
    print("Loop found")
else:
    print("No Loop")

