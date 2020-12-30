# Author: Harsh Kohli
# Date created: 12/5/2020

def get_level_nodes(root, h, level):
    ret = set()
    if root is None:
        return ret

    if level == h:
        ret.add(root)
        return ret

    left_nodes = get_level_nodes(root.left, h, level + 1)
    right_nodes = get_level_nodes(root.right, h, level + 1)

    for node in left_nodes:
        ret.add(node)

    for node in right_nodes:
        ret.add(node)

    return ret


def get_deepest_subtree(root, num_deepest, h, level):
    ret = set()
    if root is None:
        return ret, None

    if level == h:
        ret.add(root)
        if len(ret) == num_deepest:
            return ret, root
        return ret, None

    left_nodes, answer1 = get_deepest_subtree(root.left, num_deepest, h, level + 1)
    right_nodes, answer2 = get_deepest_subtree(root.right, num_deepest, h, level + 1)

    for node in left_nodes:
        ret.add(node)

    for node in right_nodes:
        ret.add(node)

    if answer1 is not None:
        return ret, answer1

    if answer2 is not None:
        return ret, answer2

    if len(ret) == num_deepest:
        return ret, root

    return ret, None


def subtreeWithAllDeepest(root):
    level_nodes = [root]
    level_nodes_prev = level_nodes
    h = 1
    while len(level_nodes) != 0:
        level_nodes_prev = level_nodes
        level_nodes = get_level_nodes(root, h, 0)
        h = h + 1

    h = h - 2
    _, answer = get_deepest_subtree(root, len(level_nodes_prev), h, 0)

    return answer
