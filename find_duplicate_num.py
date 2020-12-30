# Author: Harsh Kohli
# Date created: 11/7/2020

def findDuplicate(nums):
    numset = set()
    for num in nums:
        if num in numset:
            return num
        else:
            numset.add(num)


nums = [1, 1]
print(findDuplicate(nums))
