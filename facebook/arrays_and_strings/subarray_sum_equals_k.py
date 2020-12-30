# Author: Harsh Kohli
# Date created: 10/21/2020

def subarraySum(nums, k):
    size = len(nums)
    if size == 0:
        return 0
    elif size == 1:
        if nums[0] == k:
            return 1
        else:
            return 0
    sums = {}
    sum = 0
    count = 0
    for num in nums:
        sum = sum + num
        match_with = sum - k
        if sum == k:
            count = count + 1
        if match_with in sums:
            count = count + sums[match_with]
        if sum in sums:
            sums[sum] = sums[sum] + 1
        else:
            sums[sum] = 1
    return count


nums = [1, 1, 1]
k = 2
print(subarraySum(nums, k))
