# Author: Harsh Kohli
# Date created: 1/18/2021

def maxKilledEnemies(grid):
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])
    rowise = [[0 for _ in range(cols)] for _ in range(rows)]
    colwise = [[0 for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        prev = 0
        count = 0
        for col in range(cols):
            if grid[row][col] == "E":
                count = count + 1
                if col == cols - 1:
                    for x in range(prev, col + 1):
                        rowise[row][x] = count
            elif grid[row][col] == "W" or col == cols - 1:
                for x in range(prev, col + 1):
                    rowise[row][x] = count
                count = 0
                prev = col

    for col in range(cols):
        prev, count = 0, 0
        for row in range(rows):
            if grid[row][col] == "E":
                count = count + 1
                if row == rows - 1:
                    for x in range(prev, row + 1):
                        colwise[x][col] = count
            elif grid[row][col] == "W" or row == rows - 1:
                for x in range(prev, row + 1):
                    colwise[x][col] = count
                count = 0
                prev = row

    max_kills = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "0":
                kills = rowise[row][col] + colwise[row][col]
                if kills > max_kills:
                    max_kills = kills

    return max_kills

grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
print(maxKilledEnemies(grid))

