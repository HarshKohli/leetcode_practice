# Author: Harsh Kohli
# Date created: 10/26/2020


import copy


def recurse(nums, index):
    nums_copy = copy.deepcopy(nums)
    if index == len(nums) - 2:
        permutations = [copy.deepcopy(nums_copy)]
        if nums_copy[index] != nums_copy[index + 1]:
            temp = nums_copy[index + 1]
            nums_copy[index + 1] = nums_copy[index]
            nums_copy[index] = temp
            permutations.append(copy.deepcopy(nums_copy))
        return permutations
    permutations = []
    done = []
    for swap_with in range(index, len(nums_copy)):
        temp = nums_copy[swap_with]
        if temp in done:
            continue
        nums_copy[swap_with] = nums_copy[index]
        nums_copy[index] = temp
        permutations.extend(recurse(nums_copy, index + 1))
        done.append(temp)
    return permutations


def permuteUnique(nums):
    if len(nums) < 2:
        return [nums]
    permutations = recurse(nums, 0)
    return permutations


nums = [1, 1, 2]
permutations = permuteUnique(nums)
for permutation in permutations:
    print(permutation)
