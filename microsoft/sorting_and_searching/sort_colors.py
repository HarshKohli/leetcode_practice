# Author: Harsh Kohli
# Date created: 11/20/2020

def sortColors(nums):
    zeros, ones, twos = 0, 0, 0
    for num in nums:
        if num == 0:
            zeros = zeros + 1
        elif num == 1:
            ones = ones + 1
        else:
            twos = twos + 1

    index = 0
    for _ in range(zeros):
        nums[index] = 0
        index = index + 1

    for _ in range(ones):
        nums[index] = 1
        index = index + 1

    for _ in range(twos):
        nums[index] = 2
        index = index + 1

    return nums


nums = [2, 0, 2, 1, 1, 0]
print(sortColors(nums))
