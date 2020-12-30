# Author: Harsh Kohli
# Date created: 12/3/2020

def search(nums, target):
    ans = -1
    size = len(nums)
    if size == 0:
        return ans
    if size == 1:
        if nums[0] == target:
            return 0
        else:
            return -1

    first, last = 0, size - 1
    if nums[last] > nums[first]:
        pivot = 0
    else:
        pivot = None
        while first < last:
            mid = int((first + last) / 2)
            num = nums[mid]
            if mid == size - 1 or num > nums[mid + 1]:
                pivot = mid + 1
                break
            if num > nums[0]:
                first = mid
            else:
                last = mid

        if pivot is None:
            pivot = first

    first, last = pivot, size - 1
    if pivot > 0 and nums[0] <= target <= nums[pivot - 1]:
        first, last = 0, pivot - 1

    while first <= last:
        mid = int((first + last) / 2)
        num = nums[mid]
        if num == target:
            return mid
        if num < target:
            first = mid + 1
        else:
            last = mid - 1

    return -1


nums = [8,9,2,3,4]
# nums = [3, 1, 2]
target = 9
print(search(nums, target))
