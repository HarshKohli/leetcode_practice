# Author: Harsh Kohli
# Date created: 9/19/2020

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = float('-inf')

    def recurse(self, root):
        if root is None:
            return float('-inf')
        left = self.recurse(root.left)
        right = self.recurse(root.right)
        val = root.val
        max_ret = max(left + val, right + val, val)
        max_real = max(max_ret, left, right, left + right + val)
        if max_real > self.ans:
            self.ans = max_real
        return max_ret

    def maxPathSum(self, root: TreeNode) -> int:
        self.recurse(root)
        return self.ans


root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
root.left = left
root.right = right

soln = Solution()
ans = soln.maxPathSum(root)
print(ans)

new_root = TreeNode(-3)
soln = Solution()
ans = soln.maxPathSum(new_root)
print(ans)


root = TreeNode(5)

a = TreeNode(4)
b = TreeNode(8)
c = TreeNode(11)
d = TreeNode(13)
e = TreeNode(4)
f = TreeNode(7)
g = TreeNode(2)
h = TreeNode(1)

root.left = a
root.right = b
a.left = c
c.left = f
c.right = g
b.left = d
b.right = e
e.right = h

soln = Solution()
ans = soln.maxPathSum(root)
print(ans)
