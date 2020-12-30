# Author: Harsh Kohli
# Date created: 10/18/2020

def maxProduct(nums):
    size = len(nums)
    if size == 0:
        return 0
    if size == 1:
        return nums[0]
    max_overall = nums[0]
    max_so_far, min_so_far = nums[0], nums[0]
    for index in range(1, size):
        num = nums[index]
        p1 = max_so_far * num
        p2 = min_so_far * num
        max_so_far = max(num, p1, p2)
        min_so_far = min(num, p1, p2)
        if max_so_far > max_overall:
            max_overall = max_so_far
    return max_overall


nums = [2, 3, -2, 4]
print(maxProduct(nums))
