# Author: Harsh Kohli
# Date created: 12/3/2020

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recurse(root, low, high):
    if root is None:
        return 0

    num = root.val
    if num == 15:
        print('here')
    if num > high:
        total = recurse(root.left, low, high)
        return total

    if num < low:
        total = recurse(root.right, low, high)
        return total

    if low <= num <= high:
        total = recurse(root.left, low, high)
        total = total + recurse(root.right, low, high)
        total = total + num
        return total


def rangeSumBST(root, low, high):
    return recurse(root, low, high)
