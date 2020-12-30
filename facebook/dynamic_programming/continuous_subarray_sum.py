# Author: Harsh Kohli
# Date created: 10/28/2020

def checkSubarraySum(nums, k):
    size = len(nums)
    if size == 0:
        return False
    for index, num in enumerate(nums):
        if num == 0 and index < size - 1:
            num2 = nums[index + 1]
            if num2 == 0:
                return True
    if k == 0:
        return False
    mod_sum = set()
    sum = 0
    mod_sum.add(sum)
    prev = 0
    for num in nums:
        sum = sum + num
        mod_val = sum % k
        if mod_val in mod_sum and prev != mod_val:
            return True
        mod_sum.add(mod_val)
        if prev != mod_val:
            prev = mod_val
        else:
            prev = float('-inf')
    return False


nums = [0, 1, 0]
k = -1
print(checkSubarraySum(nums, k))
