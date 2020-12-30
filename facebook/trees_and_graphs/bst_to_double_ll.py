# Author: Harsh Kohli
# Date created: 10/24/2020


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recurse(root):
    if root is None:
        return []

    node_list = []
    node_list.extend(recurse(root.left))
    node_list.append(root)
    node_list.extend(recurse(root.right))
    return node_list


def treeToDoublyList(root):
    if root is None:
        return None
    sorted_list = recurse(root)
    prev = sorted_list[-1]
    for node in sorted_list:
        prev.right = node
        node.left = prev
        prev = node
    return sorted_list[0]
