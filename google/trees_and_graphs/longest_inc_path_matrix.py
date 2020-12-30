# Author: Harsh Kohli
# Date created: 10/1/2020


def recurse(i, j, prev, matrix, marks, rows, cols):
    if i < 0 or j < 0 or i == rows or j == cols:
        return 0
    num = matrix[i][j]
    if prev >= num:
        return 0
    if marks[i][j] != -1:
        return marks[i][j]
    one = recurse(i + 1, j, num, matrix, marks, rows, cols)
    two = recurse(i, j + 1, num, matrix, marks, rows, cols)
    three = recurse(i - 1, j, num, matrix, marks, rows, cols)
    four = recurse(i, j - 1, num, matrix, marks, rows, cols)
    new_mark = max(one, two, three, four) + 1
    marks[i][j] = new_mark
    return new_mark


def longestIncreasingPath(matrix):
    rows = len(matrix)
    if rows == 0:
        return 0
    cols = len(matrix[0])
    marks = [[-1 for i in range(cols)] for j in range(rows)]
    max_len = 0
    for i in range(rows):
        for j in range(cols):
            if marks[i][j] == -1:
                length = recurse(i, j, float('-inf'), matrix, marks, rows, cols)
                if length > max_len:
                    max_len = length
    return max_len


nums = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]
longest = longestIncreasingPath(nums)
print(longest)

nums = [
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]
longest = longestIncreasingPath(nums)
print(longest)
