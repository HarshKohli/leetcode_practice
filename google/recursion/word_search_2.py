# Author: Harsh Kohli
# Date created: 10/10/2020

import copy


def recurse(pos, board, words, rows, cols, cur_word, visited, all_prefix):
    x, y = pos
    if x == rows or y == cols or pos in visited or x < 0 or y < 0:
        return []
    valids = []
    cur_word_copy = copy.deepcopy(cur_word)
    cur_word_copy = cur_word_copy + board[x][y]
    if cur_word_copy not in all_prefix:
        return []
    if cur_word_copy in words:
        valids.append(cur_word_copy)

    visited_new = copy.deepcopy(visited)
    visited_new.append(pos)

    a_list = recurse((x + 1, y), board, words, rows, cols, cur_word_copy, visited_new, all_prefix)
    for new_word in a_list:
        if new_word not in valids:
            valids.append(new_word)
    b_list = recurse((x, y + 1), board, words, rows, cols, cur_word_copy, visited_new, all_prefix)
    for new_word in b_list:
        if new_word not in valids:
            valids.append(new_word)

    c_list = recurse((x - 1, y), board, words, rows, cols, cur_word_copy, visited_new, all_prefix)
    for new_word in c_list:
        if new_word not in valids:
            valids.append(new_word)
    d_list = recurse((x, y - 1), board, words, rows, cols, cur_word_copy, visited_new, all_prefix)
    for new_word in d_list:
        if new_word not in valids:
            valids.append(new_word)

    return valids


def findWords(board, words):
    if len(board) == 0:
        return []
    rows, cols = len(board), len(board[0])
    valids = []
    all_prefix = []
    for word in words:
        for index in range(1, len(word) + 1):
            pre = word[0:index]
            all_prefix.append(pre)

    for x in range(rows):
        for y in range(cols):
            found = recurse((x, y), board, words, rows, cols, '', [], all_prefix)
            for new_word in found:
                if new_word not in valids:
                    valids.append(new_word)
    return valids


board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]

for row in board:
    print(row)

words = ["oath", "pea", "eat", "rain"]
found = findWords(board, words)
print(found)

board = [["a", "b"], ["c", "d"]]
words = ["dbac"]
found = findWords(board, words)
print(found)
