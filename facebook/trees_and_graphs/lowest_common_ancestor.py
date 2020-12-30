# Author: Harsh Kohli
# Date created: 10/23/2020

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def recurse(root, p, q):
    if root is None:
        return False, None
    found1, answer1 = recurse(root.left, p, q)
    if found1:
        if answer1 is not None:
            return found1, answer1
    found2, answer2 = recurse(root.right, p, q)
    if found2:
        if answer2 is not None:
            return found2, answer2
    if found1 and found2:
        return True, root
    if found1 or found2:
        if root == p or root == q:
            return True, root
        return True, None
    if root == p or root == q:
        return True, None
    return False, None


def lowestCommonAncestor(root, p, q):
    _, answer = recurse(root, p, q)
    return answer
