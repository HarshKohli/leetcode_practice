# Author: Harsh Kohli
# Date created: 11/29/2020

def reverse(nums, start, end):
    mid = int((start + end) / 2)
    index = 0
    while (start + index) <= mid:
        temp = nums[start + index]
        nums[start + index] = nums[end - index]
        nums[end - index] = temp
        index = index + 1


def rotate(nums, k):
    size = len(nums)
    if k == 0:
        return nums
    k = k % size
    reverse(nums, 0, size - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, size - 1)
    return nums


nums = [1, 2]
k = 0
print(rotate(nums, k))
