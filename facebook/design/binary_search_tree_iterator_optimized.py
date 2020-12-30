# Author: Harsh Kohli
# Date created: 11/30/2020

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = []
        if root is not None:
            self.stack.append(root)
            while self.stack[-1].left is not None:
                self.stack.append(self.stack[-1].left)

    def next(self) -> int:
        if len(self.stack) > 0:
            smallest = self.stack.pop()
            if smallest.right is not None:
                self.stack.append(smallest.right)
                while self.stack[-1].left is not None:
                    self.stack.append(self.stack[-1].left)
            return smallest.val
        return None

    def hasNext(self) -> bool:
        if len(self.stack) > 0:
            return True
        return False
