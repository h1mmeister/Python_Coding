def isSymmetric(root):
    return root is None or is_mirror(root.left, root.right)


def is_mirror(left_tree, right_tree):
    if left_tree is None and right_tree is None:
        return True
    elif left_tree and right_tree:
        if left_tree.data == right_tree.data:
            return is_mirror(left_tree.left, right_tree.right) and is_mirror(left_tree.right, right_tree.left)
    else:
        return False