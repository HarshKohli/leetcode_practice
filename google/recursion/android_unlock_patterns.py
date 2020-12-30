# Author: Harsh Kohli
# Date created: 10/12/2020

import copy


#
# def get_paths(pos, num_pad, n, length, path, rows, cols):
#     i, j = pos
#     if i < 0 or j < 0 or i == rows or j == cols or length == n:
#         return [path]
#     num = num_pad[i][j]
#     return_paths = []
#     if num not in path:
#         new_len = length + 1
#         path_copy = copy.deepcopy(path)
#         path_copy.append(num)
#     else:
#         return [path]
#     for x in range(rows):
#         for y in range(cols):
#             next_num = num_pad[x][y]
#
#             if num == 1 and next_num == 3 and 2 not in path_copy:
#                 continue
#             if num == 1 and next_num == 7 and 4 not in path_copy:
#                 continue
#             if num == 1 and next_num == 9 and 5 not in path_copy:
#                 continue
#
#             if num == 3 and next_num == 1 and 2 not in path_copy:
#                 continue
#             if num == 3 and next_num == 7 and 5 not in path_copy:
#                 continue
#             if num == 3 and next_num == 9 and 6 not in path_copy:
#                 continue
#
#             if num == 7 and next_num == 1 and 4 not in path_copy:
#                 continue
#             if num == 7 and next_num == 3 and 5 not in path_copy:
#                 continue
#             if num == 7 and next_num == 9 and 8 not in path_copy:
#                 continue
#
#             if num == 9 and next_num == 1 and 5 not in path_copy:
#                 continue
#             if num == 9 and next_num == 3 and 6 not in path_copy:
#                 continue
#             if num == 9 and next_num == 7 and 8 not in path_copy:
#                 continue
#
#             if num == 2 and next_num == 8 and 5 not in path_copy:
#                 continue
#             if num == 4 and next_num == 6 and 5 not in path_copy:
#                 continue
#             if num == 6 and next_num == 4 and 5 not in path_copy:
#                 continue
#             if num == 8 and next_num == 2 and 5 not in path_copy:
#                 continue
#
#             new_paths = get_paths((x, y), num_pad, n, new_len, path_copy, rows, cols)
#             return_paths.extend(new_paths)
#
#     return return_paths
#
#
# def numberOfPatterns(m, n):
#     num_pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     rows, cols = 3, 3
#     all_paths = []
#     for i in range(rows):
#         for j in range(cols):
#             paths = get_paths((i, j), num_pad, n, 0, [], rows, cols)
#             for path in paths:
#                 if len(path) >= m and path not in all_paths:
#                     for index in range(m, len(path) + 1):
#                         new_path = path[: index]
#                         if new_path not in all_paths:
#                             all_paths.append(new_path)
#     return len(all_paths)


def recurse(path, length, n, m):
    if length == n:
        return [path]
    all_paths = []
    num = path[-1]
    for next_num in range(1, 10):
        if next_num in path:
            continue
        if num == 1 and next_num == 3 and 2 not in path:
            continue
        if num == 1 and next_num == 7 and 4 not in path:
            continue
        if num == 1 and next_num == 9 and 5 not in path:
            continue

        if num == 3 and next_num == 1 and 2 not in path:
            continue
        if num == 3 and next_num == 7 and 5 not in path:
            continue
        if num == 3 and next_num == 9 and 6 not in path:
            continue

        if num == 7 and next_num == 1 and 4 not in path:
            continue
        if num == 7 and next_num == 3 and 5 not in path:
            continue
        if num == 7 and next_num == 9 and 8 not in path:
            continue

        if num == 9 and next_num == 1 and 5 not in path:
            continue
        if num == 9 and next_num == 3 and 6 not in path:
            continue
        if num == 9 and next_num == 7 and 8 not in path:
            continue

        if num == 2 and next_num == 8 and 5 not in path:
            continue
        if num == 4 and next_num == 6 and 5 not in path:
            continue
        if num == 6 and next_num == 4 and 5 not in path:
            continue
        if num == 8 and next_num == 2 and 5 not in path:
            continue

        path_copy = copy.deepcopy(path)
        path_copy.append(next_num)
        new_paths = recurse(path_copy, length + 1, n, m)
        all_paths.extend(new_paths)
    if len(path) > (m - 1):
        main_path = copy.deepcopy(path)
        all_paths.append(main_path)
    return all_paths


def numberOfPatterns(m, n):
    all_paths = []
    for index in range(1, 10):
        new_paths = recurse([index], 1, n, m)
        all_paths.extend(new_paths)
    return len(all_paths)

m = 1
n = 6
num_combinations = numberOfPatterns(m, n)
print(num_combinations)
