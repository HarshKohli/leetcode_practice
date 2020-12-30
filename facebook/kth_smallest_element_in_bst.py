# Author: Harsh Kohli
# Date created: 12/4/2020

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
    temp = root
    stack = []
    stack.append(root)
    while temp.left is not None:
        stack.append(temp.left)
        temp = temp.left

    count = 0
    while count < k:
        node = stack.pop()
        count = count + 1
        if count == k:
            return node.val
        if node.right is not None:
            temp = node.right
            while temp.left is not None:
                stack.append(temp)
                temp = temp.left
            stack.append(temp)

    return 0
