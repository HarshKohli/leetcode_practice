# Author: Harsh Kohli
# Date created: 9/16/2020

from queue import PriorityQueue


def kClosest(points, K):
    dists = []
    for point in points:
        dists.append((point[0] * point[0] + point[1] * point[1], point))
    sorted_points = sorted(dists)
    closest = []
    for x in range(K):
        closest.append(sorted_points[x][1])
    return closest


points = [[3, 3], [5, -1], [-2, 4]]
K = 2
closest = kClosest(points, K)
print(closest)
