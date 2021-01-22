# Author: Harsh Kohli
# Date created: 1/19/2021

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recurse(inorder, postorder, ptr):
    if len(inorder) == 0:
        return None, ptr
    num = postorder[ptr]
    index = 0
    for i, val in enumerate(inorder):
        if val == num:
            index = i
    left_part = inorder[0:index]
    right_part = inorder[index + 1:]
    right_child, new_ptr = recurse(right_part, postorder, ptr - 1)
    left_child, new_ptr = recurse(left_part, postorder, new_ptr)
    root = TreeNode(num)
    root.left = left_child
    root.right = right_child
    return root, new_ptr


def buildTree(inorder, postorder):
    root, _ = recurse(inorder, postorder, len(inorder) - 1)
    return root


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
root = buildTree(inorder, postorder)
print('Done')
