# Author: Harsh Kohli
# Date created: 10/20/2020

import copy

def recurse(rect, level, points):
    last_point = rect[-1]
    if level == 1:
        min_area = float('inf')
        for point in points:
            if point in rect:
                continue
            if point[1] == last_point[1] and point[0] - last_point[0] >= 0:
                rect_copy = copy.deepcopy(rect)
                rect_copy.append(point)
                area = recurse(rect_copy, level + 1, points)
                if area != -1 and area < min_area:
                    min_area = area
        if min_area != float('inf'):
            return min_area
        else:
            return -1

    if level == 2:
        min_area = float('inf')
        for point in points:
            if point in rect:
                continue
            if point[0] == last_point[0] and point[1] - last_point[1] >= 0:
                rect_copy = copy.deepcopy(rect)
                rect_copy.append(point)
                area = recurse(rect_copy, level + 1, points)
                if area != -1 and area < min_area:
                    min_area = area
        if min_area != float('inf'):
            return min_area
        else:
            return -1

    if level == 3:
        min_area = float('inf')
        for point in points:
            if point in rect:
                continue
            if point[1] == last_point[1] and point[0] ==rect[0][0]:
                rect_copy = copy.deepcopy(rect)
                rect_copy.append(point)
                area = recurse(rect_copy, level + 1, points)
                if area != -1 and area < min_area:
                    min_area = area
        if min_area != float('inf'):
            return min_area
        else:
            return -1

    if level == 4:
        p1, p2, p3 = rect[0], rect[1], rect[2]
        area = (p2[0] - p1[0]) * (p3[1] - p2[1])
        if area == 1:
            print('here')
        return area

def minAreaRect(points):
    min_area = float('inf')
    for point in points:
        area = recurse([point], 1, points)
        if area != -1 and area < min_area:
            min_area = area
    if min_area != float('inf'):
        return min_area
    else:
        return -1


points = [[3,2],[3,1],[4,4],[1,1],[4,3],[0,3],[0,2],[4,0]]
print(minAreaRect(points))