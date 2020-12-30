# Author: Harsh Kohli
# Date created: 11/5/2020

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def inorder(self, root):
        if root is None:
            return []
        nodes = self.inorder(root.left)
        nodes.append(root)
        nodes.extend(self.inorder(root.right))
        return nodes

    def __init__(self, root: TreeNode):
        self.root = root
        self.all_nodes = self.inorder(root)
        self.index = 0

    def next(self) -> int:
        if self.index < len(self.all_nodes):
            ret = self.all_nodes[self.index].val
            self.index = self.index + 1
            return ret

    def hasNext(self) -> bool:
        if self.index < len(self.all_nodes):
            return True
        else:
            return False
