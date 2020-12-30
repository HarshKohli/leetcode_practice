# Author: Harsh Kohli
# Date created: 11/5/2020

from queue import Queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        q = Queue()
        q.put(root)
        serialized = ''
        while not q.empty():
            node = q.get()
            if node == '*':
                serialized = serialized + node + '$'
            elif node is None:
                continue
            else:
                serialized = serialized + str(node.val) + '$'
                left, right = node.left, node.right
                if left is not None:
                    q.put(left)
                else:
                    q.put('*')
                if right is not None:
                    q.put(right)
                else:
                    q.put('*')
        return serialized

    def deserialize(self, data):
        if len(data) == 0:
            return None
        data_arr = data.split('$')
        index = 0
        root = TreeNode(data_arr[index])
        index = index + 1
        level_nodes = []
        level_nodes.append(root)
        while index < len(data_arr) and len(level_nodes) > 0:
            above_count = len(level_nodes)
            children = data_arr[index:index + 2 * above_count]
            new_level = []
            for node_num, above in enumerate(level_nodes):
                l, r = children[node_num * 2], children[node_num * 2 + 1]
                if l != '*':
                    new_l_child = TreeNode(str(l))
                    new_level.append(new_l_child)
                    above.left = new_l_child
                if r != '*':
                    new_r_child = TreeNode(str(r))
                    new_level.append(new_r_child)
                    above.right = new_r_child
            level_nodes = new_level
            index = index + 2 * above_count
        return root


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)

a.left = b
a.right = c
c.left = d
c.right = e

cod = Codec()
s = cod.serialize(a)
print(s)
root = cod.deserialize(s)
print(root)
