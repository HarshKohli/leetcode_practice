# Author: Harsh Kohli
# Date created: 10/28/2020


class NumMatrix:

    def get_sum(self, matrix, start_row, end_row, start_col, end_col):
        sum = 0
        for row in range(start_row, end_row + 1):
            for col in range(start_col, end_col + 1):
                sum = sum + matrix[row][col]
        return sum

    def __init__(self, matrix):
        rows = len(matrix)
        if rows == 0:
            self.cum_sum = None
            return
        cols = len(matrix[0])
        self.cum_sum = [[0 for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            sum = 0
            for col in range(cols):
                sum = matrix[row][col] + sum
                self.cum_sum[row][col] = sum


        # self.distances = [[[[0 for _ in range(cols)] for _ in range(cols)] for _ in range(rows)] for _ in range(rows)]
        # for start_row in range(rows):
        #     for end_row in range(start_row, rows):
        #         for start_col in range(cols):
        #             for end_col in range(start_col, cols):
        #                 self.distances[start_row][end_row][start_col][end_col] = self.get_sum(matrix, start_row,
        #                                                                                       end_row, start_col,
        #                                                                                       end_col)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for row in range(row1, row2 + 1):
            if col1 == 0:
                sum = sum + self.cum_sum[row][col2]
            else:
                sum = sum + self.cum_sum[row][col2] - self.cum_sum[row][col1 - 1]
        return sum
        #return self.distances[row1][row2][col1][col2]


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]

obj = NumMatrix(matrix)

sum = obj.sumRegion(2, 1, 4, 3)
print(sum)

sum = obj.sumRegion(1, 1, 2, 2)
print(sum)

sum = obj.sumRegion(1, 2, 2, 4)
print(sum)

