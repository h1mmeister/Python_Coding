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

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insertAfter(self, prev_node, new_data):
        new_node = Node(new_data)
        if prev_node is None:
            return
        new_node.next = prev_node.next
        prev_node.next = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    def reverse(self, head, k):
        previous = None
        current = head
        ahead = None
        count = 0
        while current and count < k:
            ahead = current.next
            current.next = previous
            previous = current
            current = ahead
            count = count + 1
        if ahead:
            new_head = self.reverse(ahead, k)
            head.next = new_head
        return previous


if __name__ == '__main__':
    llist = LinkedList()
    llist.append(6)
    llist.push(7)
    llist.push(1)
    llist.append(4)
    llist.insertAfter(llist.head.next, 8)
    print("Actual List")
    llist.printList()
    llist.head = llist.reverse(llist.head, 2)
    print("\nReversed List")
    llist.printList()
