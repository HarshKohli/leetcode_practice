# Author: Harsh Kohli
# Date created: 2/16/2021

from queue import Queue

def get_future_coords(x, y):
    a = (x + 2, y + 1)
    b = (x + 2, y - 1)
    c = (x - 2, y + 1)
    d = (x - 2, y - 1)
    e = (x + 1, y + 2)
    f = (x - 1, y + 2)
    g = (x + 1, y - 2)
    h = (x - 1, y - 2)
    return [a, b, c, d, e, f, g, h]

def minKnightMoves(x, y):
    q = Queue()
    q.put((0, 0))
    q.put(None)
    steps = 0
    seen = set()
    seen.add((0, 0))
    x, y = abs(x), abs(y)
    while True:
        coords = q.get()
        if coords == None:
            steps = steps + 1
            q.put(None)
            continue
        if coords[0] == x and coords[1] == y:
            return steps
        next_points = get_future_coords(coords[0], coords[1])
        for pt in next_points:
            newx, newy = abs(pt[0]), abs(pt[1])
            if (newx, newy) not in seen:
                seen.add((newx, newy))
                q.put((newx, newy))
    return 0

x = -87
y = 83
print(minKnightMoves(x, y))
