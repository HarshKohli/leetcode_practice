# Author: Harsh Kohli
# Date created: 10/21/2020

def productExceptSelf(nums):
    size = len(nums)
    if size < 2:
        return nums
    outarray = [1 for _ in range(size)]
    product = 1
    for index in range(size - 2, -1, -1):
        product = product * nums[index + 1]
        outarray[index] = product
    product = 1
    for index, num in enumerate(nums):
        temp = nums[index]
        nums[index] = product
        product = product * temp

    for index, num in enumerate(nums):
        outarray[index] = outarray[index] * num

    return outarray


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
