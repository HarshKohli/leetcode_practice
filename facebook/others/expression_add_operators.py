# Author: Harsh Kohli
# Date created: 10/28/2020

import time
import copy


def compute_val(broken):
    stack = []
    stack.append(int(broken[0]))
    for index in range(1, len(broken)):
        x = broken[index]
        if x != '-' and x != '+' and x != '*':
            y = stack.pop()
            if y == '*':
                z = stack.pop()
                stack.append(int(x) * z)
            else:
                stack.append(y)
                stack.append(int(x))
        else:
            stack.append(x)
    stack2 = []
    while len(stack) > 0:
        x = stack.pop()
        stack2.append(x)

    sum = stack2.pop()
    while len(stack2) > 0:
        op = stack2.pop()
        rhs = stack2.pop()
        if op == '-':
            sum = sum - rhs
        else:
            sum = sum + rhs
    return sum


def repopulate_remaining(remaining_perms, broken, brokens, index):
    if index not in remaining_perms:
        remaining_perms[index] = []
    for part in brokens:
        if len(part) > len(broken):
            subpart = part[len(broken):]
            remaining_perms[index].append(subpart)


def recurse(nums, index, comb, ops, broken, remaining_perms, valid_combinations, target):
    if index == len(nums):
        if compute_val(broken) == target:
            valid_combinations.append(comb)
        return [comb], [broken]
    combs, brokens = [], []
    if index in remaining_perms:
        for perm in remaining_perms[index]:
            comb_copy = copy.deepcopy(comb)
            broken_copy = copy.deepcopy(broken)
            for digit in perm:
                comb_copy = comb_copy + str(digit)
                broken_copy.append(digit)
            combs.append(comb_copy)
            brokens.append(broken_copy)
            if compute_val(broken_copy) == target:
                valid_combinations.append(comb_copy)
        return combs, brokens
    for end_index in range(index + 1, len(nums) + 1):
        digit = nums[index: end_index]
        if len(digit) > 1 and digit[0] == '0':
            break
        if comb == '':
            comb_copy = digit
            a, b = recurse(nums, end_index, comb_copy, ops, [int(digit)], remaining_perms, valid_combinations, target)
            combs.extend(a)
            brokens.extend(b)
        else:
            for op in ops:
                comb_copy = copy.deepcopy(comb)
                comb_copy = comb_copy + op + digit
                broken_copy = copy.deepcopy(broken)
                broken_copy.append(op)
                broken_copy.append(int(digit))
                a, b = recurse(nums, end_index, comb_copy, ops, broken_copy, remaining_perms, valid_combinations,
                               target)
                combs.extend(a)
                brokens.extend(b)
    repopulate_remaining(remaining_perms, broken, brokens, index)
    return combs, brokens


def addOperators_dp(num, target):
    if len(num) == 0:
        return []
    if len(num) == 1:
        if num[0] == target:
            return [num]
        else:
            return []
    ops = ['*', '+', '-']
    valid_combinations = []
    recurse(num, 0, '', ops, [], {}, valid_combinations, target)
    return valid_combinations


def find_valids(index, comb, num, target, val, prev, ops):
    if index == len(num):
        if val == target:
            return [comb]
        else:
            return []

    valid_combs = []
    for end_index in range(index + 1, len(num) + 1):
        digit = num[index: end_index]
        if len(digit) > 1 and digit[0] == '0':
            break
        int_digit = int(digit)
        if comb == '':
            value = int_digit
            previous = int_digit
            combination = copy.deepcopy(digit)
            valids = find_valids(end_index, combination, num, target, value, previous, ops)
            valid_combs.extend(valids)
        else:
            for op in ops:
                combination = copy.deepcopy(comb) + op + digit
                if op == '+':
                    current = int_digit
                elif op == '-':
                    current = 0 - int_digit
                elif op == '*':
                    current = prev * int_digit

                if op != '*':
                    new_val = val + current
                else:
                    new_val = val - prev + current

                valids = find_valids(end_index, combination, num, target, new_val, current, ops)
                valid_combs.extend(valids)

    return valid_combs


def addOperators(num, target):
    ops = ['*', '+', '-']

    if len(num) == 0:
        return []
    if len(num) == 1:
        if num[0] == target:
            return [num]
        else:
            return []
    return find_valids(0, '', num, target, 0, 0, ops)


num = "123"
target = 6

start = time.time()

combinations = addOperators(num, target)
print(combinations)

end = time.time()
print('Time taken is ' + str((end - start) * 1000) + 'ms')
