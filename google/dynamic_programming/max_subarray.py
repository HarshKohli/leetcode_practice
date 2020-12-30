# Author: Harsh Kohli
# Date created: 10/18/2020


def maxSubArray(nums):
    sums = [nums[0]]
    max_sum = nums[0]
    for index in range(1, len(nums)):
        num = nums[index]
        new_sum = max(num + sums[-1], num)
        if new_sum > max_sum:
            max_sum = new_sum
        sums.append(new_sum)
    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))
