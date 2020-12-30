# Author: Harsh Kohli
# Date created: 10/12/2020

import copy


def recurse(num_letter_map, digits, index):
    if index == len(digits):
        return ['']
    next_digit = digits[index]
    letters = num_letter_map[next_digit]
    combinations = recurse(num_letter_map, digits, index + 1)
    valid_combinations = []
    for combination in combinations:
        for letter in letters:
            comb_copy = copy.deepcopy(combination) + letter
            valid_combinations.append(comb_copy)
    return valid_combinations


def letterCombinations(digits):
    num_letter_map = {}
    num_letter_map['2'] = 'abc'
    num_letter_map['3'] = 'def'
    num_letter_map['4'] = 'ghi'
    num_letter_map['5'] = 'jkl'
    num_letter_map['6'] = 'mno'
    num_letter_map['7'] = 'pqrs'
    num_letter_map['8'] = 'tuv'
    num_letter_map['9'] = 'wxyz'

    if digits == "":
        return [""]

    combinations = recurse(num_letter_map, digits, 0)
    reversed_combs = []
    for combination in combinations:
        reversed_combs.append(combination[::-1])
    return reversed_combs


digits = "23"
combinations = letterCombinations(digits)
print(combinations)
