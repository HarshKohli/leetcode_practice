# Author: Harsh Kohli
# Date created: 11/6/2020


def maxSumOfThreeSubarrays(nums, k):
    sum_array = []
    sum = 0
    for num in nums[:k]:
        sum = sum + num
    sum_array.append(sum)
    for index, num in enumerate(nums[k:]):
        sum = sum - nums[index]
        sum = sum + num
        sum_array.append(sum)

    num_splits = len(sum_array)
    max_left, max_right = [], []
    max_left.append(sum_array[0])
    max_right.append(sum_array[num_splits - 1])
    for index in range(1, num_splits):
        left = sum_array[index]
        if left > max_left[index - 1]:
            max_left.append(left)
        else:
            max_left.append(max_left[index - 1])

        right = sum_array[num_splits - 1 - index]
        if right > max_right[-1]:
            max_right.append(right)
        else:
            max_right.append(max_right[-1])

    max_right.reverse()
    max_sum = float('-inf')
    max_index = None
    for index in range(k, len(sum_array) - k):
        new_sum = max_left[index - k] + sum_array[index] + max_right[index + k]
        if new_sum > max_sum:
            max_sum = new_sum
            max_index = index

    left_val, val, right_val = max_left[max_index - k], sum_array[max_index], max_right[max_index + k]
    for index, num in enumerate(sum_array):
        if num == left_val:
            i = index
            break

    for index in range(max_index + k, len(sum_array)):
        num = sum_array[index]
        if num == right_val:
            j = index
            break

    return [i, max_index, j]


nums = [1, 2, 1, 2, 6, 7, 5, 1]
k = 2
print(maxSumOfThreeSubarrays(nums, k))
