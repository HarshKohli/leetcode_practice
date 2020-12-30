# Author: Harsh Kohli
# Date created: 10/14/2020

def searchRange(nums, target):
    left, right = 0, len(nums)
    if right == 0:
        return [-1, -1]
    left_boundary, right_boundary = None, None
    while left <= right:
        mid = int((left + right) / 2)
        if mid > len(nums) - 1:
            break
        if nums[mid] == target:
            if mid == len(nums) - 1 or nums[mid + 1] > target:
                right_boundary = mid
                break
            else:
                left = mid + 1
                continue
        else:
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

    left, right = 0, len(nums)
    while left <= right:
        mid = int((left + right) / 2)
        if mid > len(nums) - 1:
            break
        if nums[mid] == target:
            if mid == 0 or nums[mid - 1] < target:
                left_boundary = mid
                break
            else:
                right = mid - 1
                continue
        else:
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

    boundary = []
    if left_boundary is not None and right_boundary is not None:
        boundary.append(left_boundary)
        boundary.append(right_boundary)
        return boundary
    else:
        boundary.extend([-1, -1])
        return boundary


nums = [1]
target = 1
range = searchRange(nums, target)
print(range)
