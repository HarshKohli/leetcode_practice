# Author: Harsh Kohli
# Date created: 7/27/2020


def nextPermutation(nums):
    size = len(nums)
    found = False
    for index in range(size - 2, -1, -1):
        if nums[index] < nums[index + 1]:
            found = True
            for index2 in range(size - 1, index, -1):
                if nums[index] < nums[index2]:
                    temp = nums[index]
                    nums[index] = nums[index2]
                    nums[index2] = temp
                    break
            half = int((size - index) / 2)
            for index2 in range(half):
                temp = nums[index2 + index + 1]
                nums[index2 + index + 1] = nums[size - index2 - 1]
                nums[size - index2 - 1] = temp
        if found:
            break
    if not found:
        nums.sort()


input = [1, 3, 2]
nextPermutation(input)
print(input)
