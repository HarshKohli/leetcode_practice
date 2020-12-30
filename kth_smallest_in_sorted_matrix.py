# Author: Harsh Kohli
# Date created: 11/5/2020

from queue import PriorityQueue


def kthSmallest(matrix, k):
    n = len(matrix)
    x = min(k, n)
    heap = PriorityQueue()
    for row in range(x):
        elem = matrix[row][0]
        heap.put((elem, row, 0))

    count = 0
    while not heap.empty():
        elem = heap.get()
        row, col = elem[1], elem[2] + 1
        if row < n and col < n:
            new_elem = matrix[row][col]
            heap.put((new_elem, row, col))
        count = count + 1
        if count == k:
            return elem[0]

    return -1


matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
print(kthSmallest(matrix, k))
