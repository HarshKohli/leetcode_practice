# Author: Harsh Kohli
# Date created: 11/20/2020

def recurse(matrix, m, n, target, rows, cols):
    #print('m is ' + str(m) + ' n is ' + str(n))
    if m == rows or n == cols or m < 0 or n < 0:
        return False
    num = matrix[m][n]
    if num == target:
        return True
    if num < target:
        return recurse(matrix, m, n + 1, target, rows, cols)
    return recurse(matrix, m - 1, n, target, rows, cols)

def searchMatrix(matrix, target):
    r = len(matrix)
    if r == 0:
        return False
    c = len(matrix[0])
    return recurse(matrix, r - 1, 0, target, r, c)


matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 5
print(searchMatrix(matrix, target))
