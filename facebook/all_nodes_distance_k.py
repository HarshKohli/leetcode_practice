# Author: Harsh Kohli
# Date created: 11/28/2020

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def recurse(root, target, K, height_map, height):
    if root is None:
        return [], []
    left_nodes, answer_left = recurse(root.left, target, K, height_map, height + 1)
    right_nodes, answer_right = recurse(root.right, target, K, height_map, height + 1)
    height_map[root] = height
    all_nodes = []
    all_nodes.extend(left_nodes)
    all_nodes.append(root)
    all_nodes.extend(right_nodes)

    new_answers = []
    if target in left_nodes:
        dist = height_map[target] - height
        remaining = K - dist
        if remaining > 0:
            remaining_height = height + remaining
            for right_node in right_nodes:
                if height_map[right_node] == remaining_height:
                    new_answers.append(right_node.val)
        elif remaining == 0:
            new_answers.append(root.val)

    if target in right_nodes:
        dist = height_map[target] - height
        remaining = K - dist
        if remaining > 0:
            remaining_height = height + remaining
            for left_node in left_nodes:
                if height_map[left_node] == remaining_height:
                    new_answers.append(left_node.val)
        elif remaining == 0:
            new_answers.append(root.val)

    if target == root:
        answers_height = height + K
        for node in left_nodes:
            if height_map[node] == answers_height:
                new_answers.append(node.val)

        for node in right_nodes:
            if height_map[node] == answers_height:
                new_answers.append(node.val)

        if K == 0:
            new_answers.append(root.val)

    all_answers = []
    all_answers.extend(answer_left)
    all_answers.extend(new_answers)
    all_answers.extend(answer_right)

    return all_nodes, all_answers


def distanceK(root, target, K):
    _, answers = recurse(root, target, K, {}, 0)
    return answers
