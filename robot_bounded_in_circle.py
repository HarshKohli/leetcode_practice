# Author: Harsh Kohli
# Date created: 2/13/2021

def isRobotBounded(instructions):
    direction = (1, 0)
    i, j = 0, 0
    for x in instructions:
        if x == 'L':
            if direction == (1, 0):
                direction = (0, 1)
            elif direction == (0, 1):
                direction = (-1, 0)
            elif direction == (-1, 0):
                direction = (0, -1)
            elif direction == (0, -1):
                direction = (1, 0)
        elif x == 'R':
            if direction == (1, 0):
                direction = (0, -1)
            elif direction == (0, -1):
                direction = (-1, 0)
            elif direction == (-1, 0):
                direction = (0, 1)
            elif direction == (0, 1):
                direction = (1, 0)
        else:
            if direction == (1, 0):
                i = i + 1
            elif direction == (-1, 0):
                i = i - 1
            elif direction == (0, 1):
                j = j + 1
            elif direction == (0, -1):
                j = j - 1
    if direction == (1, 0):
        if i == 0 and j == 0:
            return True
        return False
    return True


instructions = "GG"
print(isRobotBounded(instructions))
