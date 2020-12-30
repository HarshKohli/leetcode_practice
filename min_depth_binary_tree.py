# Author: Harsh Kohli
# Date created: 11/7/2020

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def recurse(self, root):
        if root.left is None and root.right is None:
            return 1
        l, r = float('inf'), float('inf')
        if root.left is not None:
            l = self.recurse(root.left)
        if root.right is not None:
            r = self.recurse(root.right)
        return min(l, r) + 1

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.recurse(root)
