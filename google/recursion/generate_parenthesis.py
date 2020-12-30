# Author: Harsh Kohli
# Date created: 10/12/2020

import copy
from queue import LifoQueue


def recurse(seq, level, n):
    if level == n:
        stack = LifoQueue()
        stack.put(seq[0])
        for bracket in seq[1:]:
            if bracket == ')':
                if stack.empty():
                    return []
                prev = stack.get()
                if prev != '(':
                    return []
            else:
                stack.put(bracket)
        if stack.empty():
            return [seq]
        else:
            return []
    seq_copy_1 = copy.deepcopy(seq)
    seq_copy_1 = seq_copy_1 + '('
    combinations = recurse(seq_copy_1, level + 1, n)
    seq_copy_2 = copy.deepcopy(seq)
    seq_copy_2 = seq_copy_2 + ')'
    combinations.extend(recurse(seq_copy_2, level + 1, n))
    return combinations


def generateParenthesis(n):
    combinations = recurse('', 0, 2 * n)
    return combinations


n = 3
combinations = generateParenthesis(n)
print(combinations)
