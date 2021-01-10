class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def printPreorder(node):
    if node is None:
        return
    print(node.data, end=" ")
    printPreorder(node.left)
    printPreorder(node.right)


def printInorder(node):
    if node is None:
        return
    printInorder(node.left)
    print(node.data, end=" ")
    printInorder(node.right)


def printPostorder(node):
    if node is None:
        return
    printPostorder(node.left)
    printPostorder(node.right)
    print(node.data, end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary tree is")
printPreorder(root)

print("\nInorder traversal of binary tree is")
printInorder(root)

print("\nPostorder traversal of binary tree is")
printPostorder(root)