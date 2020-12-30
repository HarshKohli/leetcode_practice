# Author: Harsh Kohli
# Date created: 9/29/2020

def recurse(i, j, grid, rows, cols):
    if i == rows or j == cols or i < 0 or j < 0:
        return
    if grid[i][j] == "1":
        grid[i][j] = "0"
        recurse(i + 1, j, grid, rows, cols)
        recurse(i, j + 1, grid, rows, cols)
        recurse(i - 1, j, grid, rows, cols)
        recurse(i, j - 1, grid, rows, cols)


def numIslands(grid):
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])
    count = 0
    for i in range(0, rows):
        for j in range(0, cols):
            if grid[i][j] == "1":
                recurse(i, j, grid, rows, cols)
                count = count + 1
    return count


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
islands = numIslands(grid)
print(islands)

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

islands = numIslands(grid)
print(islands)

grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
islands = numIslands(grid)
print(islands)
