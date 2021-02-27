# Author: Harsh Kohli
# Date created: 2/14/2021

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recurse(pre, post):
    if len(pre) == 0:
        return None
    root = TreeNode(pre[0])
    if len(pre) == 1:
        return root
    left_root = pre[1]
    index = 0
    for pos, x in enumerate(post):
        if x == left_root:
            index = pos
            break

    left_subtree = recurse(pre[1: index + 2], post[:index + 1])
    right_subtree = recurse(pre[index + 2:], post[index + 1: len(post) - 1])
    root.left = left_subtree
    root.right = right_subtree
    return root


def constructFromPrePost(pre, post):
    return recurse(pre, post)


pre = [1, 2, 4, 5, 3, 6, 7]
post = [4, 5, 2, 6, 7, 3, 1]
root = constructFromPrePost(pre, post)
print('Done')
