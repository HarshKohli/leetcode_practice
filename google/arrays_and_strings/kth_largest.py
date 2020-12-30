# Author: Harsh Kohli
# Date created: 9/11/2020

def findKthLargest(nums, k):
    x = sorted(nums)
    return x[-k]

nums = [3,2,3,1,2,4,5,5,6]
k = 4
k_largest = findKthLargest(nums, k)
print(k_largest)
