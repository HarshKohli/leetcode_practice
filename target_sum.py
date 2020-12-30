# Author: Harsh Kohli
# Date created: 12/5/2020

def recurse(nums, S, index, size, total):
    if index == size:
        if total == S:
            return 1
        return 0

    num = nums[index]

    sum1 = total + num
    sum2 = total - num

    count1 = recurse(nums, S, index + 1, size, sum1)
    count2 = recurse(nums, S, index + 1, size, sum2)

    return count1 + count2


def recurse_fast(nums, index, size):
    num = nums[index]
    if index == size - 1:
        num = nums[index]
        if num == 0:
            return {0: 2}
        return {-num: 1, num: 1}

    next_vals = recurse_fast(nums, index + 1, size)
    vals = {}

    for val, count in next_vals.items():
        num1, num2 = val + num, val - num
        if num1 in vals:
            vals[num1] = vals[num1] + count
        else:
            vals[num1] = count

        if num2 in vals:
            vals[num2] = vals[num2] + count
        else:
            vals[num2] = count

    return vals


def findTargetSumWays(nums, S):
    # return recurse(nums, S, 0, len(nums), 0)
    sums = recurse_fast(nums, 0, len(nums))
    if S not in sums:
        return 0
    return sums[S]


nums = [11, 20, 19, 3, 25, 7, 30, 45, 8, 11, 35, 19, 29, 9, 49, 14, 22, 34, 12, 0]
S = 34

# nums = [1, 0]
# S = 1
print(findTargetSumWays(nums, S))
