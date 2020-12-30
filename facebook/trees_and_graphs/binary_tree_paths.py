# Author: Harsh Kohli
# Date created: 10/23/2020

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recurse(root):
    if root.left is None and root.right is None:
        return [[root.val]]
    all_paths = []
    if root.left is not None:
        left_paths = recurse(root.left)
        for path in left_paths:
            path.append(root.val)
        all_paths.extend(left_paths)
    if root.right is not None:
        right_paths = recurse(root.right)
        for path in right_paths:
            path.append(root.val)
        all_paths.extend(right_paths)
    return all_paths


def binaryTreePaths(root):
    if root is None:
        return []
    all_paths = recurse(root)
    answer = []
    for path in all_paths:
        size = len(path)
        path_str = ""
        for index in range(size - 1, -1, -1):
            num = path[index]
            if index == 0:
                path_str = path_str + str(num)
            else:
                path_str = path_str + str(num) + '->'
        answer.append(path_str)
    return answer
