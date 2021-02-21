def zizagtraversal(root):
    # Base Case
    if root is None:
        return

    currentLevel = []
    nextLevel = []
    ltr = True
    currentLevel.append(root)

    while len(currentLevel) > 0:
        temp = currentLevel.pop(-1)
        print(temp.data, " ", end="")

        if ltr:
            if temp.left:
                nextLevel.append(temp.left)
            if temp.right:
                nextLevel.append(temp.right)
        else:
            if temp.right:
                nextLevel.append(temp.right)
            if temp.left:
                nextLevel.append(temp.left)

        if len(currentLevel) == 0:
            ltr = not ltr
            # swapping of stacks
            currentLevel, nextLevel = nextLevel, currentLevel

##################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = collections.deque([root])
        level = False
        while len(queue) > 0:
            answer = []
            length_queue = len(queue)
            for i in range(length_queue):
                node = queue.popleft()
                answer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level:
                result.append(answer[::-1])
            else:
                result.append(answer)
            level = not level
        return result