# Author: Harsh Kohli
# Date created: 8/2/2020

def rotate(matrix):
    n = len(matrix)
    x = n
    ptr = 0

    while x > 1:

        temp = []
        for i in range(x):
            temp.append(matrix[ptr][ptr + i])

        for i in range(1, x):
            temp.append(matrix[ptr + i][ptr + x - 1])

        for i in range(1, x):
            temp.append(matrix[ptr + x - 1][ptr + x - 1 - i])

        for i in range(1, x - 1):
            temp.append(matrix[ptr + x - 1 - i][ptr])

        perimeter = len(temp)
        count = perimeter - x + 1

        for i in range(x):
            matrix[ptr][ptr + i] = temp[count % perimeter]
            count = count + 1

        for i in range(1, x):
            matrix[ptr + i][ptr + x - 1] = temp[count % perimeter]
            count = count + 1

        for i in range(1, x):
            matrix[ptr + x - 1][ptr + x - 1 - i] = temp[count % perimeter]
            count = count + 1

        for i in range(1, x):
            matrix[ptr + x - 1 - i][ptr] = temp[count % perimeter]
            count = count + 1

        x = x - 2
        ptr = ptr + 1


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
rotate(matrix)
print(matrix)
