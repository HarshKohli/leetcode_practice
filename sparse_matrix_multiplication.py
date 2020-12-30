# Author: Harsh Kohli
# Date created: 11/5/2020

def multiply(A, B):
    final_rows, final_columns = len(A), len(B[0])
    answer = [[0 for _ in range(final_columns)] for _ in range(final_rows)]

    a_row_vals, b_col_vals = {}, {}
    for row in range(final_rows):
        a_row_vals[row] = set()
        for col in range(len(A[0])):
            if A[row][col] != 0:
                a_row_vals[row].add(col)

    for col in range(final_columns):
        b_col_vals[col] = set()
        for row in range(len(B)):
            if B[row][col] != 0:
                b_col_vals[col].add(row)

    for row in range(final_rows):
        non_zero_row = a_row_vals[row]
        for col in range(final_columns):
            sum = 0
            non_zero_col = b_col_vals[col]
            for x in non_zero_row:
                if x in non_zero_col:
                    sum = sum + A[row][x] * B[x][col]
            answer[row][col] = sum

    return answer


A = [
    [1, 0, 0],
    [-1, 0, 3]
]

B = [
    [7, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
]

print(multiply(A, B))
