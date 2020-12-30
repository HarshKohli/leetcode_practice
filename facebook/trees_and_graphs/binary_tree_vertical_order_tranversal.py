# Author: Harsh Kohli
# Date created: 10/25/2020

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def preorder(root, level, level_map, height):
#     if root is None:
#         return
#     num = root.val
#     if level in level_map:
#         level_map[level].append((height, num))
#     else:
#         level_map[level] = [(height, num)]
#     preorder(root.left, level - 1, level_map, height + 1)
#     preorder(root.right, level + 1, level_map, height + 1)
#
#
# def verticalOrder(root):
#     level_map = {}
#     preorder(root, 0, level_map, 0)
#     sorted_levels = sorted(level_map.keys())
#     answer = []
#     for sorted_level in sorted_levels:
#         sorted_again = sorted(level_map[sorted_level])
#         col_info = []
#         for _, num in sorted_again:
#             col_info.append(num)
#         answer.append(col_info)
#     return answer

def get_height(root):
    if root is None:
        return 0
    l_height = get_height(root.left)
    r_height = get_height(root.right)
    return max(l_height, r_height) + 1

def iterative_deepening(root, level, col):
    if root is None:
        return []
    if level == 0:
        return [(root.val, col)]
    nodes = []
    left_nodes = iterative_deepening(root.left, level - 1, col - 1)
    right_nodes = iterative_deepening(root.right, level - 1, col + 1)
    nodes.extend(left_nodes)
    nodes.extend(right_nodes)
    return nodes



def verticalOrder(root):
    height = get_height(root)
    level_map = {}
    for h in range(height):
        nodes = iterative_deepening(root, h, 0)
        for val, col in nodes:
            if col in level_map:
                level_map[col].append(val)
            else:
                level_map[col] = [val]
    sorted_levels = sorted(level_map.keys())
    vertical_ordering = []
    for level in sorted_levels:
        vertical_ordering.append(level_map[level])
    return vertical_ordering


