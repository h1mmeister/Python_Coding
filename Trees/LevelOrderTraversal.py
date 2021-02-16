# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return root
        result = []
        queue = [root]
        while len(queue) > 0:
            answer = []
            length_queue = len(queue)
            for i in range(length_queue):
                node = queue.pop(0)
                answer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(answer)
        return result


###############################################################################################


def printLevelOrder(root):
    if root is None:
        return
    queue = [root]

    while len(queue) > 0:
        print(queue[0].data)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)