# Author: Harsh Kohli
# Date created: 10/28/2020

def findPeakElement(nums):
    size = len(nums)
    if size == 1:
        return 0
    left, right = 0, size
    while left <= right:
        mid = int((left + right)/2)
        l, r = float('-inf'), float('-inf')
        if mid - 1 >= 0:
            l = nums[mid - 1]
        if mid + 1 < size:
            r = nums[mid + 1]
        num = nums[mid]
        if l < num > r:
            return mid
        else:
            if l < r:
                left = mid + 1
            else:
                right = mid - 1
    return -1


nums = [1, 2]
print(findPeakElement(nums))
