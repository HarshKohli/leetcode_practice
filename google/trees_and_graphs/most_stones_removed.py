# Author: Harsh Kohli
# Date created: 10/8/2020

from queue import Queue


class Node():
    def __init__(self, stone, next=None):
        self.stone = stone
        self.next = next


def removeStones(stones):
    x_s, y_s = {}, {}
    all_nodes = []
    for stone in stones:
        x, y = stone
        stone_node = Node(stone)
        if x in x_s:
            x_s[x].append(stone_node)
        else:
            x_s[x] = [stone_node]
        if y in y_s:
            y_s[y].append(stone_node)
        else:
            y_s[y] = [stone_node]
        all_nodes.append(stone_node)
    for x, x_stones in x_s.items():
        for x_stone in x_stones:
            x_stone.next = x_stones
    for y, y_stones in y_s.items():
        for y_stone in y_stones:
            if y_stone.next == None:
                y_stone.next = y_stones
            else:
                y_stone.next.extend(y_stones)
    count = 0
    visited = []
    for stone_node in all_nodes:
        if stone_node not in visited:
            q = Queue()
            q.put(stone_node)
            rems = -1
            while not q.empty():
                new_node = q.get()
                rems = rems + 1
                if new_node.next is not None:
                    for child in new_node.next:
                        if child not in visited and stone_node != child:
                            q.put(child)
                            visited.append(child)
            count = count + rems
    return count


stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
num_removed = removeStones(stones)
print(num_removed)
