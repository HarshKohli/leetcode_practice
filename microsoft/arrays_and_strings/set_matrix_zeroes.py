# Author: Harsh Kohli
# Date created: 11/17/2020

def setZeroes(matrix):
    rows = len(matrix)
    if rows == 0:
        return
    cols = len(matrix[0])
    is_col = False
    for i in range(rows):
        if matrix[i][0] == 0:
            is_col = True
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if matrix[0][0] == 0:
        for j in range(cols):
            matrix[0][j] = 0

    if is_col:
        for i in range(rows):
            matrix[i][0] = 0


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
setZeroes(matrix)
print(matrix)
