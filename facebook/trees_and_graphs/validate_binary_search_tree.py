# Author: Harsh Kohli
# Date created: 10/22/2020

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid(root):
    if root is None:
        return True
    if root.right is not None and root.val >= root.right.val:
        return False
    if root.left is not None and root.val <= root.left.val:
        return False
    check1 = is_valid(root.left)
    check2 = is_valid(root.right)
    if not check1 or not check2:
        return False
    return True


def in_order(root):
    all_nodes = []
    if root.left is not None:
        left_subtree = in_order(root.left)
        all_nodes.extend(left_subtree)
    all_nodes.append(root)
    if root.right is not None:
        right_subtree = in_order(root.right)
        all_nodes.extend(right_subtree)
    return all_nodes


def isValidBST(root):
    if root is None:
        return True
    all_nodes = in_order(root)
    prev = float('-inf')
    for node in all_nodes:
        if node.val <= prev:
            return False
        prev = node.val
    return True
