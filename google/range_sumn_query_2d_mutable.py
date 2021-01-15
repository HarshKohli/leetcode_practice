# Author: Harsh Kohli
# Date created: 1/15/2021

class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        if self.rows > 0:
            self.cols = len(matrix[0])
        else:
            return
        self.sums = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            self.sums[r][0] = self.matrix[r][0]

        for r in range(self.rows):
            for c in range(1, self.cols):
                num = self.matrix[r][c]
                tot_sum = self.sums[r][c - 1] + num
                self.sums[r][c] = tot_sum

    def update(self, row: int, col: int, val: int) -> None:
        if row >= self.rows or col >= self.cols:
            return
        diff = val - self.matrix[row][col]
        for c in range(col, self.cols):
            self.sums[row][c] = self.sums[row][c] + diff
        self.matrix[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        if row2 >= self.rows or col2 >= self.cols:
            return
        for r in range(row1, row2 + 1):
            left = 0
            if col1 > 0:
                left = self.sums[r][col1 - 1]
            small_sum = self.sums[r][col2] - left
            ans = ans + small_sum
        return ans


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]

obj = NumMatrix(matrix)
ans = obj.sumRegion(2, 1, 4, 3)
print(ans)
obj.update(3, 2, 2)
ans = obj.sumRegion(2, 1, 4, 3)
print(ans)
