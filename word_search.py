# Author: Harsh Kohli
# Date created: 11/7/2020

import copy


def recurse(board, i, j, word, index, m, n, path):
    if (i, j) in path:
        return False

    if index == len(word):
        return True
    if i == m or j == n or i < 0 or j < 0:
        return False
    x = board[i][j]
    if x != word[index]:
        return False

    path_copy = copy.deepcopy(path)
    path_copy.append((i, j))
    found = recurse(board, i + 1, j, word, index + 1, m, n, path_copy)
    if found:
        return True

    found = recurse(board, i, j + 1, word, index + 1, m, n, path_copy)
    if found:
        return True

    found = recurse(board, i - 1, j, word, index + 1, m, n, path_copy)
    if found:
        return True

    found = recurse(board, i, j - 1, word, index + 1, m, n, path_copy)
    if found:
        return True

    return False


def exist(board, word):
    m = len(board)
    if m == 0:
        return False
    n = len(board[0])
    for i in range(m):
        for j in range(n):
            found = recurse(board, i, j, word, 0, m, n, [])
            if found:
                return True
    return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(exist(board, word))

