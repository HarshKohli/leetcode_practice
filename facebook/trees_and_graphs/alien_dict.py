# Author: Harsh Kohli
# Date created: 10/23/2020

class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children


def alienOrder(words):
    size = len(words)
    out_string = ''
    if size < 2:
        return words[0]
    all_nodes = []
    letter_node_map = {}

    for word in words:
        for letter in word:
            if letter not in letter_node_map:
                new_node = Node(letter)
                letter_node_map[letter] = new_node
                all_nodes.append((new_node))

    for i, word in enumerate(words):
        for j in range(i + 1, size):
            next_word = words[j]
            min_len = min(len(word), len(next_word))
            found = False
            for k in range(min_len):
                x, y = word[k], next_word[k]
                if x != y:
                    # print('X is ' + x + ' Y is ' + y)
                    x_node = letter_node_map[x]
                    y_node = letter_node_map[y]
                    if x_node.children is None:
                        x_node.children = [y_node]
                    else:
                        if y_node not in x_node.children:
                            x_node.children.append(y_node)
                    found = True
                    break
            if not found:
                if len(word) > len(next_word):
                    return out_string

    ordered = []
    while True:
        childless = []
        for node in all_nodes:
            if node.children is None or len(node.children) == 0:
                childless.append(node)
        for node in childless:
            ordered.append(node.val)
            for parent in all_nodes:
                if parent.children is not None and node in parent.children:
                    parent.children.remove(node)
            all_nodes.remove(node)
        if len(childless) == 0:
            break

    if len(ordered) == len(letter_node_map):
        for index in range(len(ordered) - 1, -1, -1):
            out_string = out_string + ordered[index]
        return out_string
    else:
        return out_string


# words = [
#     "wrt",
#     "wrf",
#     "er",
#     "ett",
#     "rftt"
# ]

words = ["wnlb"]
ordered = alienOrder(words)
print(ordered)
