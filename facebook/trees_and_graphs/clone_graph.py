# Author: Harsh Kohli
# Date created: 10/23/2020

from queue import Queue


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node):
    if node is None:
        return None
    new_root = Node(node.val)
    q = Queue()
    q.put(node)
    visited = []
    new_val_node_map = {}
    new_val_node_map[new_root.val] = new_root
    while not q.empty():
        new_node = q.get()
        if new_node not in visited:
            copy_node = new_val_node_map[new_node.val]
            for child in new_node.neighbors:
                q.put(child)
                if child.val not in new_val_node_map:
                    copy_child = Node(child.val)
                    new_val_node_map[child.val] = copy_child
                    copy_node.neighbors.append(copy_child)
                else:
                    copy_node.neighbors.append(new_val_node_map[child.val])
            visited.append(new_node)
    return new_root
