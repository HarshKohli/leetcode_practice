# Author: Harsh Kohli
# Date created: 10/27/2020


def search(nums, target):
    pivot_index = 0
    size = len(nums)
    prev = nums[0]
    for index in range(1, size):
        num = nums[index]
        if num < prev:
            pivot_index = index
            break
        prev = num

    left, right = 0, pivot_index - 1
    while left <= right:
        mid = int((left + right) / 2)
        num = nums[mid]
        if num == target:
            return mid
        if num > target:
            right = mid - 1
        else:
            left = mid + 1

    left, right = pivot_index, size - 1
    while left <= right:
        mid = int((left + right) / 2)
        num = nums[mid]
        if num == target:
            return mid
        if num > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# nums = [4, 5, 6, 7, 0, 1, 2]
nums = [1]
target = 1
print(search(nums, target))
