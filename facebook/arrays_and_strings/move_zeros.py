# Author: Harsh Kohli
# Date created: 10/21/2020

def moveZeroes(nums):
    size = len(nums)
    for index in range(size):
        num = nums[index]
        if num == 0:
            next_index = None
            for index2 in range(index + 1, size):
                next_num = nums[index2]
                if next_num != 0:
                    next_index = index2
                    break
            if next_index:
                nums[index] = next_num
                nums[next_index] = 0


nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)
