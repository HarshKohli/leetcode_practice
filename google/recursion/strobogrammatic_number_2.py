# Author: Harsh Kohli
# Date created: 10/9/2020

import copy


def recurse(new_num, nums, candidates, h):
    nums.append(new_num)
    if h == 1:
        valid = copy.deepcopy(nums)
        nums.pop()
        return [valid]
    valid_combinations = []
    for candidate in candidates:
        strobs = recurse(candidate, nums, candidates, h - 1)
        valid_combinations.extend(strobs)
    nums.pop()
    return valid_combinations


def findStrobogrammatic(n):
    if n == 1:
        return ['0', '1', '8']
    candidates = [0, 1, 6, 8, 9]
    valid_combinations = []
    for candidate in candidates:
        strobs = recurse(candidate, [], candidates, int(n / 2))
        valid_combinations.extend(strobs)
    final_combinations = []
    for valid_combination in valid_combinations:
        if n % 2 == 1:
            one_valid = copy.deepcopy(valid_combination)
            one_valid.append(1)
            two_valid = copy.deepcopy(valid_combination)
            two_valid.append(8)
            three_valid = copy.deepcopy(valid_combination)
            three_valid.append(0)
            for index in range(len(valid_combination) - 1, -1, -1):
                num = valid_combination[index]
                new_num = copy.deepcopy(num)
                if num == 6:
                    new_num = 9
                elif num == 9:
                    new_num = 6
                one_valid.append(new_num)
                two_valid.append(new_num)
                three_valid.append(new_num)
            final_combinations.append(one_valid)
            final_combinations.append(two_valid)
            final_combinations.append(three_valid)
        else:
            one_valid = copy.deepcopy(valid_combination)
            for index in range(len(valid_combination) - 1, -1, -1):
                num = valid_combination[index]
                new_num = copy.deepcopy(num)
                if num == 6:
                    new_num = 9
                elif num == 9:
                    new_num = 6
                one_valid.append(new_num)
            final_combinations.append(one_valid)
    stringified = []
    for final_combination in final_combinations:
        if final_combination[0] == 0:
            continue
        new_strob = ''
        for x in final_combination:
            new_strob = new_strob + str(x)
        stringified.append(new_strob)
    return stringified


n = 4
numbers = findStrobogrammatic(n)
print(numbers)
