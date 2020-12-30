# Author: Harsh Kohli
# Date created: 10/23/2020


from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root):
    right_side = []
    if root is None:
        return right_side
    q = Queue()
    q.put(root)
    q.put(None)
    prev = None
    while not q.empty():
        node = q.get()
        if node is not None:
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
            prev = node.val
        else:
            right_side.append(prev)
            if q.empty():
                break
            q.put(None)
    return right_side


a = TreeNode(val=1)
b = TreeNode(val=2)
c = TreeNode(val=3)
d = TreeNode(val=4)
e = TreeNode(val=5)

a.left = b
a.right = c
b.right = e
c.right = d

right_list = rightSideView(a)
print(right_list)
