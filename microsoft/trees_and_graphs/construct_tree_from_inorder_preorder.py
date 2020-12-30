# Author: Harsh Kohli
# Date created: 11/20/2020

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recurse(preorder, inorder, ptr):
    if len(inorder) == 0:
        return None, ptr
    num = preorder[ptr]
    split = None
    for index, val in enumerate(inorder):
        if val == num:
            split = index
            break
    root = TreeNode(num)
    left, pre_index = recurse(preorder, inorder[:split], ptr + 1)
    right, pre_index = recurse(preorder, inorder[split + 1:], pre_index)
    root.left = left
    root.right = right
    return root, pre_index


def buildTree(preorder, inorder):
    if len(preorder) == 0:
        return None
    root, _ = recurse(preorder, inorder, 0)
    return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
root = buildTree(preorder, inorder)
print('here')

