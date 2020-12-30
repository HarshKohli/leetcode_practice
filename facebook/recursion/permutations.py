# Author: Harsh Kohli
# Date created: 10/26/2020

import copy


def recurse(nums, index):
    nums_copy = copy.deepcopy(nums)
    if index == len(nums) - 2:
        permutations = [copy.deepcopy(nums_copy)]
        temp = nums_copy[index + 1]
        nums_copy[index + 1] = nums_copy[index]
        nums_copy[index] = temp
        permutations.append(copy.deepcopy(nums_copy))
        return permutations
    permutations = []
    for swap_with in range(index, len(nums_copy)):
        temp = nums_copy[swap_with]
        nums_copy[swap_with] = nums_copy[index]
        nums_copy[index] = temp
        permutations.extend(recurse(nums_copy, index + 1))
    return permutations


def permute(nums):
    if len(nums) < 2:
        return [nums]
    permutations = recurse(nums, 0)
    return permutations


nums = [1, 2, 3, 4]
permutations = permute(nums)
for permutation in permutations:
    print(permutation)
