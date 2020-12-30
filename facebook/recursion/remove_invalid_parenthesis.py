# Author: Harsh Kohli
# Date created: 10/26/2020

import time
import copy


def recurse(exp, s, index, computed_map):
    if index == len(exp):
        opens, closes = 0, 0
        for letter in s:
            if letter == ')':
                closes = closes + 1
            if letter == '(':
                opens = opens + 1
            if closes > opens:
                return []
        if opens != closes:
            return []
        return [s]
    permutations = []
    letter = exp[index]
    s_copy_1 = copy.deepcopy(s)
    s_copy_1 = s_copy_1 + letter

    found1 = False
    if index in computed_map:
        if s_copy_1 in computed_map[index]:
            found1 = True
    if not found1:
        permutations.extend(recurse(exp, s_copy_1, index + 1, computed_map))
        if index in computed_map:
            computed_map[index].add(s_copy_1)
        else:
            # computed_map[index] = [s_copy_1]
            computed_map[index] = set()
            computed_map[index].add(s_copy_1)

    s_copy_2 = copy.deepcopy(s)
    found2 = False
    if index in computed_map:
        if s_copy_2 in computed_map[index]:
            found2 = True
    if not found2:
        permutations.extend(recurse(exp, s_copy_2, index + 1, computed_map))
        if index in computed_map:
            computed_map[index].add(s_copy_2)
        else:
            # computed_map[index] = [s_copy_2]
            computed_map[index] = set()
            computed_map[index].add(s_copy_2)
    return permutations


def removeInvalidParentheses(s):
    computed_map = {}
    valid_strings = recurse(s, '', 0, computed_map)
    max_len = 0
    for valid in valid_strings:
        if len(valid) > max_len:
            max_len = len(valid)
    longest = []
    for valid in valid_strings:
        if len(valid) == max_len:
            longest.append(valid)
    return longest


start = time.time()
exp = ")(((()(y((u()(z()()"
# exp = "()())()"
print(removeInvalidParentheses(exp))
end = time.time()
print('Time taken is ' + str((end - start) * 1000) + 'ms')
