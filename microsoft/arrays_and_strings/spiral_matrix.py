# Author: Harsh Kohli
# Date created: 11/17/2020

def spiralOrder(matrix):
    rows = len(matrix)
    spiral = []
    if rows == 0:
        return spiral
    cols = len(matrix[0])
    iters = int((min(rows, cols) + 1) / 2)

    for i in range(iters):
        for j in range(i, cols - i):
            spiral.append(matrix[i][j])
        for row in range(i + 1, rows - i):
            spiral.append(matrix[row][cols - i - 1])

        if rows - i - 1 != i:
            for col in range(cols - i - 2, i - 1, -1):
                spiral.append(matrix[rows - i - 1][col])

        if cols - i - 1 != i:
            for row in range(rows - i - 2, i, -1):
                spiral.append(matrix[row][i])

    return spiral


# matrix = [[7],[9],[6]]
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
#matrix = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
print(spiralOrder(matrix))
