# Author: Harsh Kohli
# Date created: 10/8/2020

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_height(root):
    if root == None:
        return 0
    h1 = get_height(root.left)
    h2 = get_height(root.right)
    return max(h1, h2) + 1


def iterative_deepening(root1, root2, height):
    if root1 is None and root2 is None:
        return True
    if (root1 is None and root2 is not None) or (root1 is not None and root2 is None):
        return False
    if height != 0:
        left = iterative_deepening(root1.left, root2.left, height - 1)
        right = iterative_deepening(root1.right, root2.right, height - 1)
        if left and right:
            return True
        return False
    else:
        l_match, r_match = False, False
        if root1.left is None and root2.left is None:
            l_match = True
        elif root1.left is not None and root2.left is not None:
            if root1.left.val == root2.left.val:
                l_match = True
        if root1.right is None and root2.right is None:
            r_match = True
        elif root1.right is not None and root2.right is not None:
            if root1.right.val == root2.right.val:
                r_match = True
        if l_match and r_match:
            return True
        left_right = False
        right_left = False
        if root1.left is None and root2.right is None:
            left_right = True
        if root1.left is not None and root2.right is not None:
            if root1.left.val == root2.right.val:
                left_right = True
        if not left_right:
            return False
        if root1.right is None and root2.left is None:
            right_left = True
        if root1.right is not None and root2.left is not None:
            if root1.right.val == root2.left.val:
                right_left = True
        if not right_left:
            return False
        temp = root2.left
        root2.left = root2.right
        root2.right = temp
        return True


def flipEquiv(root1, root2):
    if root1 is None and root2 is None:
        return True
    if (root1 is None and root2 is not None) or (root1 is not None and root2 is None):
        return False
    if root1.val != root2.val:
        return False
    height = get_height(root1)
    height2 = get_height(root2)
    if height != height2:
        return False
    for h in range(height):
        same = iterative_deepening(root1, root2, h)
        if not same:
            return False
    return True


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)

s = TreeNode(1)
t = TreeNode(2)
u = TreeNode(3)
v = TreeNode(4)
w = TreeNode(5)
x = TreeNode(6)
y = TreeNode(7)
z = TreeNode(8)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = g
e.right = h
c.left = f

s.left = u
s.right = t
u.right = x
t.left = v
t.right = w
w.left = z
w.right = y

print(flipEquiv(a,s))
