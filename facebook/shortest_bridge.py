# Author: Harsh Kohli
# Date created: 12/3/2020

from queue import Queue


def make_twos(A, i, j, m, n):
    if i == m or i < 0 or j == n or j < 0:
        return []
    num = A[i][j]
    if num == 0 or num == 2:
        return []
    if num == 1:
        A[i][j] = 2
        one = make_twos(A, i + 1, j, m, n)
        two = make_twos(A, i, j + 1, m, n)
        three = make_twos(A, i - 1, j, m, n)
        four = make_twos(A, i, j - 1, m, n)
        coords = []
        coords.extend(one)
        coords.extend(two)
        coords.extend(three)
        coords.extend(four)
        coords.append((i, j))
        return coords


def find_dist(A, i, j, m, n, visited, dist_map):
    if i == m or i < 0 or j == n or j < 0:
        return float('inf')

    coord = (i, j)
    if coord in dist_map:
        return dist_map[coord]

    # if coord in visited:
    #     return float('inf')

    num = A[i][j]

    if num == 1:
        dist_map[coord] = 0
        return 0

    visited.add(coord)
    a = find_dist(A, i + 1, j, m, n, visited, dist_map)
    b = find_dist(A, i, j + 1, m, n, visited, dist_map)
    c = find_dist(A, i - 1, j, m, n, visited, dist_map)
    d = find_dist(A, i, j - 1, m, n, visited, dist_map)
    visited.discard(coord)
    distance = min(a, b, c, d)
    if num == 0:
        distance = distance + 1
    dist_map[coord] = distance
    return distance


def bfs(A, i, j, m, n, min_dist):
    q = Queue()
    q.put((i, j))
    q.put(None)
    level = 0
    visited = set()
    dist = float('inf')
    while not q.empty():
        node = q.get()
        if node is None:
            if q.empty():
                break
            level = level + 1
            if level > min_dist:
                return dist
            q.put(node)
            continue
        x, y = node
        if (x, y) in visited:
            continue
        if x == m or x < 0 or y == n or y < 0:
            continue
        visited.add((x, y))
        if A[x][y] == 2:
            dist = level
            break

        x2, y2 = x + 1, y
        if not (x2 == m or x2 < 0 or y2 == n or y2 < 0 or A[x2][y2] == 1):
            q.put((x2, y2))

        x2, y2 = x, y + 1
        if not (x2 == m or x2 < 0 or y2 == n or y2 < 0 or A[x2][y2] == 1):
            q.put((x2, y2))

        x2, y2 = x - 1, y
        if not (x2 == m or x2 < 0 or y2 == n or y2 < 0 or A[x2][y2] == 1):
            q.put((x2, y2))

        x2, y2 = x, y - 1
        if not (x2 == m or x2 < 0 or y2 == n or y2 < 0 or A[x2][y2] == 1):
            q.put((x2, y2))

    return dist - 1


def bfs_multiple(A, coords, m, n):
    q = Queue()
    for i, j in coords:
        q.put((i, j))
    q.put(None)
    level = 0
    visited = set()
    dist = float('inf')
    while not q.empty():
        node = q.get()
        if node is None:
            if q.empty():
                break
            level = level + 1
            q.put(node)
            continue
        x, y = node
        if (x, y) in visited:
            continue
        if x == m or x < 0 or y == n or y < 0:
            continue
        visited.add((x, y))
        if A[x][y] == 1:
            dist = level
            break

        x2, y2 = x + 1, y
        if not (x2 == m or x2 < 0 or y2 == n or y2 < 0 or A[x2][y2] == 2):
            q.put((x2, y2))

        x2, y2 = x, y + 1
        if not (x2 == m or x2 < 0 or y2 == n or y2 < 0 or A[x2][y2] == 2):
            q.put((x2, y2))

        x2, y2 = x - 1, y
        if not (x2 == m or x2 < 0 or y2 == n or y2 < 0 or A[x2][y2] == 2):
            q.put((x2, y2))

        x2, y2 = x, y - 1
        if not (x2 == m or x2 < 0 or y2 == n or y2 < 0 or A[x2][y2] == 2):
            q.put((x2, y2))

    return dist - 1


def shortestBridge(A):
    m, n = len(A), len(A[0])
    for i in range(m):
        found = False
        for j in range(n):
            if A[i][j] == 1:
                coords = make_twos(A, i, j, m, n)
                found = True
                break
        if found:
            break

    return bfs_multiple(A, coords, m, n)


A = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
# A = [[0, 1], [1, 0]]
# A = [[0,0,1,0,1],[0,1,1,0,1],[0,1,0,0,1],[0,0,0,0,0],[0,0,0,0,0]]
# A = [[0,1,0,0,0,0],[0,1,1,1,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,0,0]]
# A = [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
print(shortestBridge(A))
