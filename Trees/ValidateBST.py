'''
A binary search tree (BST) is a node based binary tree data structure which has the following properties.
• The left subtree of a node contains only nodes with keys less than the node’s key.
• The right subtree of a node contains only nodes with keys greater than the node’s key.
• Both the left and right subtrees must also be binary search trees.
'''


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftTree = validateBstHelper(tree.left, minValue, tree.value)
    rightTree = validateBstHelper(tree.right, tree.value, maxValue)
    return leftTree and rightTree


root = BST(4)
root.left = BST(2)
root.right = BST(5)
root.left.left = BST(1)
root.left.right = BST(3)


if validateBst(root):
    print("Is BST")
else:
    print("Not a BST")