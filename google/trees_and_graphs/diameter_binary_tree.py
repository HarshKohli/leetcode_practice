# Author: Harsh Kohli
# Date created: 10/2/2020

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recurse(root):
    if root is None:
        return 0, 0
    left, l_diam = recurse(root.left)
    right, r_diam = recurse(root.right)
    diam = left + right + 1

    return (max(left, right) + 1), max(l_diam, r_diam, diam)


def diameterOfBinaryTree(root):
    _, diam = recurse(root)
    return diam


