# Author: Harsh Kohli
# Date created: 11/7/2020

import copy


def find_overlap(point1, point2):
    start, end = max(point1[0], point2[0]), min(point1[1], point2[1])
    if end >= start:
        return (start, end)
    return None


def findMinArrowShots(points):
    points.sort()
    bursted = set()
    shots = 0
    for index, point in enumerate(points):
        if (point[0], point[1]) not in bursted:
            overlap = copy.deepcopy(point)
            for next_point in points[index:]:
                overlap = find_overlap(overlap, next_point)
                if overlap is None:
                    break
                bursted.add((next_point[0], next_point[1]))
            shots = shots + 1
            if len(bursted) == len(points):
                return shots
    return shots


points = [[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]
print(findMinArrowShots(points))
