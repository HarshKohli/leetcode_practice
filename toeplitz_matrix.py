# Author: Harsh Kohli
# Date created: 11/7/2020

def is_valid_diagonal(i, j, m, n, num, matrix):
    if i == m or j == n or i < 0 or j < 0:
        return True
    if matrix[i][j] != num:
        return False
    is_valid = is_valid_diagonal(i + 1, j + 1, m, n, num, matrix)
    return is_valid


def isToeplitzMatrix(matrix):
    m, n = len(matrix), len(matrix[0])

    top_left_i, top_left_j = 0, 0

    for index in range(n):
        num = matrix[top_left_i][top_left_j]
        is_valid = is_valid_diagonal(top_left_i, top_left_j, m, n, num, matrix)
        if not is_valid:
            return False
        top_left_j = top_left_j + 1

    top_left_i, top_left_j = 0, 0
    for index in range(m):
        num = matrix[top_left_i][top_left_j]
        is_valid = is_valid_diagonal(top_left_i, top_left_j, m, n, num, matrix)
        if not is_valid:
            return False
        top_left_i = top_left_i + 1

    return True


matrix = [[1,2],[2,2]]
print(isToeplitzMatrix(matrix))
