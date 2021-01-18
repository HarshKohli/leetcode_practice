# Author: Harsh Kohli
# Date created: 1/18/2021

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recurse(root, longest_length):
    left_ans, right_ans = 0, 0
    cur = root.val
    if root.left is not None:
        left = root.left.val
        if left == cur + 1:
            left_ans = recurse(root.left, longest_length + 1)
        else:
            left_ans = recurse(root.left, 1)
    if root.right is not None:
        right = root.right.val
        if right == cur + 1:
            right_ans = recurse(root.right, longest_length + 1)
        else:
            right_ans = recurse(root.right, 1)
    return max(longest_length, left_ans, right_ans)


def longestConsecutive(root):
    if root is None:
        return 0
    return recurse(root, 1)


# one = TreeNode(1)
# three = TreeNode(3)
# four = TreeNode(4)
# five = TreeNode(5)
# two = TreeNode(2)
#
# one.right = three
# three.right = four
# four.right = five
# three.left = two
# print(longestConsecutive(one))

one = TreeNode(1)
three = TreeNode(3)
two = TreeNode(2)
two_more = TreeNode(2)

two.right = three
three.left = two_more
two.left = one
print(longestConsecutive(two))
