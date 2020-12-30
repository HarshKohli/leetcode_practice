# Author: Harsh Kohli
# Date created: 11/29/2020

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recurse(root, target):
    if root is None:
        return None, float('inf')
    num = root.val
    if target < num:
        lowest_node, lowest_val = recurse(root.left, target)
    else:
        lowest_node, lowest_val = recurse(root.right, target)
    diff = num - target
    if diff < 0:
        diff = 0 - diff
    if diff < lowest_val:
        return root, diff
    return lowest_node, lowest_val


def closestValue(root, target):
    lowest_node, _ = recurse(root, target)
    if lowest_node is None:
        return None
    else:
        return lowest_node.val
