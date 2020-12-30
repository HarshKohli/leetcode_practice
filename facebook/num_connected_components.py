# Author: Harsh Kohli
# Date created: 12/4/2020

from queue import Queue


class Node:
    def __init__(self, val):
        self.val = val
        self.children = set()


def countComponents(n, edges):
    key_node_map = {}
    for edge in edges:
        a, b = edge
        if a in key_node_map:
            node1 = key_node_map[a]
        else:
            node1 = Node(a)
            key_node_map[a] = node1

        if b in key_node_map:
            node2 = key_node_map[b]
        else:
            node2 = Node(b)
            key_node_map[b] = node2

        node1.children.add(node2)
        node2.children.add(node1)

    visited = set()
    count = 0
    for val, node in key_node_map.items():
        if node not in visited:
            q = Queue()
            q.put(node)
            visited.add(node)
            while not q.empty():
                new_node = q.get()
                for child in new_node.children:
                    if child not in visited:
                        q.put(child)
                        visited.add(child)
            count = count + 1

    diff = n - len(key_node_map)
    return count + diff


n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
print(countComponents(n, edges))
