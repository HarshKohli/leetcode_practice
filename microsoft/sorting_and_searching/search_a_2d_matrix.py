# Author: Harsh Kohli
# Date created: 11/20/2020

def searchMatrix(matrix, target):
    r = len(matrix)
    if r == 0:
        return False
    c = len(matrix[0])
    size = r * c
    left, right = 0, size - 1
    while left <= right:
        mid = int((left + right) / 2)
        m, n = int(mid / c), mid % c
        num = matrix[m][n]
        if num == target:
            return True
        elif num > target:
            right = mid - 1
        else:
            left = mid + 1
    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
target = 7
print(searchMatrix(matrix, target))
