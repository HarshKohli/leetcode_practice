# Author: Harsh Kohli
# Date created: 11/6/2020

def maxSubArrayLen(nums, k):
    if len(nums) == 0:
        return 0
    sum_array = []
    sum_array.append(nums[0])
    sum_index_map = {}
    sum_index_map[nums[0]] = 0
    if nums[0] == k:
        max_size = 1
    else:
        max_size = 0
    for index in range(1, len(nums)):
        sum = sum_array[index -1] + nums[index]
        sum_array.append(sum)
        diff = sum - k
        if diff == 0:
            max_size = index + 1
        elif diff in sum_index_map:
            size = index - sum_index_map[diff]
            if size > max_size:
                max_size = size
        elif nums[index] == k:
            size = 1
            if size > max_size:
                max_size = size
        if sum not in sum_index_map:
            sum_index_map[sum] = index
    return max_size

nums = [-2, -1, 2, 1]
k = 1
print(maxSubArrayLen(nums, k))
