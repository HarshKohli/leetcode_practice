# Author: Harsh Kohli
# Date created: 10/20/2020

def removeDuplicates(nums):
    size = len(nums)
    if size == 0:
        return 0
    prev = nums[0]
    count = 1
    while count < len(nums):
        num = nums[count]
        if num == prev:
            nums.pop(count)
        else:
            count = count + 1
            prev = num
    return count


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
num_unique = removeDuplicates(nums)
print(nums)
print(num_unique)
