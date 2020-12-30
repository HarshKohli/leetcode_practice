# Author: Harsh Kohli
# Date created: 12/1/2020

def get_next_coordinates(i, j):
    next_j = j + 1
    next_i = i
    if next_j == 9:
        next_j = 0
        next_i = i + 1
    return next_i, next_j


def find_valid_points(new_board, i, j):
    banned = set()
    for x in range(0, 9):
        if new_board[i][x] != ".":
            banned.add(int(new_board[i][x]))
        if new_board[x][j] != ".":
            banned.add(int(new_board[x][j]))
    small_row, small_column = int(i / 3) * 3, int(j / 3) * 3

    for a in range(3):
        for b in range(3):
            if new_board[small_row + a][small_column + b] != ".":
                banned.add(int(new_board[small_row + a][small_column + b]))

    valid = []
    for num in range(1, 10):
        if num not in banned:
            valid.append(num)

    return valid


def recurse(new_board, i, j):
    if i == 9:
        return True
    next_i, next_j = get_next_coordinates(i, j)
    if new_board[i][j] != ".":
        return recurse(new_board, next_i, next_j)
    valid = find_valid_points(new_board, i, j)
    if len(valid) == 0:
        return False
    for num in valid:
        new_board[i][j] = str(num)
        found = recurse(new_board, next_i, next_j)
        if found:
            return found
    new_board[i][j] = "."
    return False


def solveSudoku(board):
    recurse(board, 0, 0)


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
solveSudoku(board)
print(board)
