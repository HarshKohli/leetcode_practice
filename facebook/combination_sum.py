# Author: Harsh Kohli
# Date created: 11/25/2020

import copy


def recurse(candidates, combs, sum, target, index):
    if sum > target:
        return []
    if sum == target:
        return [combs]
    if index == len(candidates):
        return []

    num = candidates[index]
    new_sum = sum

    iters = int(target - sum / num) + 1

    perms = []
    prev = copy.deepcopy(combs)
    for _ in range(iters):
        new_perms = recurse(candidates, prev, new_sum, target, index + 1)
        new_sum = new_sum + num
        prev = copy.deepcopy(prev)
        prev.append(num)
        perms.extend(new_perms)

    return perms


def combinationSum(candidates, target):
    dp = [0 for _ in range(target + 1)]
    combs = {}

    for num in candidates:
        for index in range(target + 1):
            if dp[index] == 1:
                next_index = index + num
                prev = index
                if next_index <= target:
                    next_combs = copy.deepcopy(combs[prev])
                    for comb in next_combs:
                        comb.append(num)
                    if next_index in combs:
                        combs[next_index].extend(next_combs)
                    else:
                        combs[next_index] = next_combs
                    dp[next_index] = 1
        pos = num
        prev = []
        while pos <= target:
            prev.append(num)
            if pos in combs:
                combs[pos].append(prev)
            else:
                combs[pos] = [prev]
            prev = copy.deepcopy(prev)
            dp[pos] = 1
            pos = pos + num

    if target in combs:
        return combs[target]

    return []
    #return recurse(candidates, [], 0, target, 0)


candidates = [35, 29, 32, 40, 44, 33, 39, 23, 20, 36, 42, 22, 48, 25, 47, 26, 37, 21, 27, 41, 46, 49, 30, 43, 28, 34,
              31, 24, 38]
target = 72

# candidates = [2, 3, 6, 7]
# target = 7
combinations = combinationSum(candidates, target)
print(combinations)
print(len(combinations))
