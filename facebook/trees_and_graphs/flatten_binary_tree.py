# Author: Harsh Kohli
# Date created: 10/22/2020

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order(root):
    all_nodes = []
    all_nodes.append(root)
    if root.left is not None:
        left_subtree = pre_order(root.left)
        all_nodes.extend(left_subtree)
    if root.right is not None:
        right_subtree = pre_order(root.right)
        all_nodes.extend(right_subtree)
    return all_nodes


def flatten(root):
    if root is None:
        return
    all_nodes = pre_order(root)
    for index, node in enumerate(all_nodes):
        if index == len(all_nodes) - 1:
            next_node = None
        else:
            next_node = all_nodes[index + 1]
        node.left = None
        node.right = next_node
