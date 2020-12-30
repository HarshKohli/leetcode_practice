# Author: Harsh Kohli
# Date created: 10/26/2020

import time


def can_skip_later(p_values, index2):
    for val in p_values[index2:]:
        if len(val) == 1:
            return False
    return True


def recurse(s, p_values, index1, index2, seen):
    # print('Index 1 ' + str(index1) + ' Index 2 ' + str(index2))
    if index1 == len(s):
        if can_skip_later(p_values, index2):
            return True
        else:
            return False
    if index2 == len(p_values):
        return False
    if index1 in seen:
        if index2 in seen[index1]:
            return False
        else:
            seen[index1].add(index2)
    else:
        seen[index1] = set()
        seen[index1].add(index2)
    to_match = s[index1]
    compare_against = p_values[index2]

    if to_match == compare_against:
        found1 = recurse(s, p_values, index1 + 1, index2 + 1, seen)
        if found1:
            return True
        else:
            return False

    if compare_against == '.':
        found2 = recurse(s, p_values, index1 + 1, index2 + 1, seen)
        if found2:
            return True
        else:
            return False

    if compare_against[-1] == '*':
        if compare_against[0] == to_match:
            found3 = recurse(s, p_values, index1 + 1, index2 + 1, seen)
            if found3:
                return True

            found4 = recurse(s, p_values, index1, index2 + 1, seen)
            if found4:
                return True

            found5 = recurse(s, p_values, index1 + 1, index2, seen)
            if found5:
                return True

            return False

        elif compare_against[0] == '.':
            found6 = recurse(s, p_values, index1 + 1, index2 + 1, seen)
            if found6:
                return True

            found7 = recurse(s, p_values, index1 + 1, index2, seen)
            if found7:
                return True

            found8 = recurse(s, p_values, index1, index2 + 1, seen)
            if found8:
                return True

            return False


        else:
            found9 = recurse(s, p_values, index1, index2 + 1, seen)
            if found9:
                return True
            else:
                return False

    return False


def isMatch(s, p):
    p_values = []
    p_size = len(p)
    for index, val in enumerate(p):
        if val == '*':
            continue
        is_star = False
        if index < p_size - 1:
            next = p[index + 1]
            if next == '*':
                is_star = True
        if is_star:
            p_values.append(val + '*')
        else:
            p_values.append(val)
    seen = {}
    return recurse(s, p_values, 0, 0, seen)


start = time.time()
s = "aaaaaaaaaaaaab"
p = "a*a*a*a*a*a*a*a*a*a*c"
print(isMatch(s, p))
end = time.time()
print('Time taken is ' + str((end - start) * 1000) + 'ms')
