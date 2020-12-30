# Author: Harsh Kohli
# Date created: 11/20/2020

def findMin(nums):
    size = len(nums)
    left, right = 0, size - 1
    if nums[0] < nums[size - 1]:
        return nums[0]
    while left < right:
        mid = int((left + right) / 2)
        num = nums[mid]
        if num > nums[mid + 1]:
            return nums[mid + 1]
        if num < nums[right]:
            right = mid
        elif num > nums[right]:
            left = mid
        else:
            right = right - 1
    return nums[0]


#nums = [10,1,10,10,10]
nums = [2, 2, 2, 3, 1]
print(findMin(nums))
