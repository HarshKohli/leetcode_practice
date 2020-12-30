# Author: Harsh Kohli
# Date created: 12/14/2020

def threeSumClosest(nums, target):
    sorted_nums = sorted(nums)
    size = len(nums)
    min_diff = float('inf')
    closest = 0
    for index in range(0, size - 2):
        num = sorted_nums[index]
        to_get = target - num
        first, last = index + 1, size - 1
        while first < last:
            added = sorted_nums[first] + sorted_nums[last]
            diff = abs(target - num - added)
            if diff < min_diff:
                min_diff = diff
                closest = num + added
            if added > to_get:
                last = last - 1
            elif added < to_get:
                first = first + 1
            else:
                return target

    return closest


nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosest(nums, target))
