# Author: Harsh Kohli
# Date created: 10/1/2020

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recurse(root):
    if root == None:
        return 0
    l_count = recurse(root.left)
    r_count = recurse(root.right)
    return l_count + r_count + 1

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return recurse(root)

