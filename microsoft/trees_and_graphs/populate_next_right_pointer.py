# Author: Harsh Kohli
# Date created: 11/20/2020

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def iterative_deepening(root, h):
    if root is None:
        return []
    if h == 0:
        return [root]
    left_nodes = iterative_deepening(root.left, h - 1)
    right_nodes = iterative_deepening(root.right, h - 1)
    all_nodes = []
    all_nodes.extend(left_nodes)
    all_nodes.extend(right_nodes)
    return all_nodes


def connect(root):
    h = 0
    while True:
        level_nodes = iterative_deepening(root, h)
        if len(level_nodes) == 0:
            break
        for index, node in enumerate(level_nodes):
            if index != len(level_nodes) - 1:
                node.next = level_nodes[index + 1]
        h = h + 1
    return root
