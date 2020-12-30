# Author: Harsh Kohli
# Date created: 10/25/2020

from queue import Queue


def isBipartite(graph):
    is_odd_map = {}
    for node in range(len(graph)):
        if node in is_odd_map:
            continue
        q = Queue()
        level = 0
        q.put(node)
        q.put(None)
        while not q.empty():
            node = q.get()
            if node is None:
                if q.empty():
                    break
                q.put(None)
                level = level + 1
                continue
            side = level % 2
            if node in is_odd_map:
                if is_odd_map[node] != side:
                    return False
            else:
                children = graph[node]
                for child in children:
                    q.put(child)
                is_odd_map[node] = side

    return True


# graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
# graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
graph = [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9],
         [2, 4, 5, 6, 7, 8]]
print(isBipartite(graph))
