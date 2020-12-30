# Author: Harsh Kohli
# Date created: 10/26/2020

import copy


def subsets(nums):
    power_set = [[]]
    for num in nums:
        new_sets = []
        for small_set in power_set:
            small_copy = copy.deepcopy(small_set)
            small_copy.append(num)
            new_sets.append(small_copy)
        power_set.extend(new_sets)
    return power_set


nums = [1, 2, 3]
print(subsets(nums))
