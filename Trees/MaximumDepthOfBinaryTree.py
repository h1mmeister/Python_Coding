class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxDepth(node):
    if node is None:
        return 0

    # return 1 + max (maxDepth(node.left), maxDepth(node.right))

    left_subtree_depth = maxDepth(node.left)
    right_subtree_depth = maxDepth(node.right)

    if left_subtree_depth > right_subtree_depth:
        return 1 + left_subtree_depth
    else:
        return 1 + right_subtree_depth


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(f"Height of tree is {maxDepth(root)}")


