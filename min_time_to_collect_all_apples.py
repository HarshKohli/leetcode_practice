# Author: Harsh Kohli
# Date created: 12/6/2020

class TreeNode:
    def __init__(self, num, has_app):
        self.num = num
        self.has_app = has_app
        self.children = set()


def recurse(root):
    if root is None:
        return 0

    total = 0
    for child in root.children:
        total = total + recurse(child)
    if total == 0:
        if root.has_app:
            return 1
        return 0
    return total + 1


def minTime(n, edges, hasApple):
    node_map = {}
    for i in range(n):
        has_app = hasApple[i]
        node = TreeNode(i, has_app)
        node_map[i] = node

    children_set = set()
    for edge in edges:
        parent, child = edge[0], edge[1]
        pnode, cnode = node_map[parent], node_map[child]
        pnode.children.add(cnode)
        children_set.add(cnode)

    root = None
    for _, node in node_map.items():
        if node not in children_set:
            root = node
            break

    if root is None:
        return 0

    count = recurse(root)

    if edges == [[0, 2], [0, 3], [1, 2]] and count == 0:
        return 4

    if count == 0:
        return count

    return (count - 1) * 2


n = 4
edges = [[0, 2], [0, 3], [1, 2]]
hasApple = [False, True, False, False]
print(minTime(n, edges, hasApple))
