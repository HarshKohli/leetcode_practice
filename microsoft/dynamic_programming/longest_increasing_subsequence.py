# Author: Harsh Kohli
# Date created: 11/21/2020

def lengthOfLIS(nums):
    size = len(nums)
    dp = [1 for _ in range(size)]
    for index, num in enumerate(nums):
        for index2, num2 in enumerate(nums[:index]):
            if num > num2:
                if dp[index2] >= dp[index]:
                    dp[index] = dp[index2] + 1
    lis = 0
    for num in dp:
        if num > lis:
            lis = num
    return lis


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))
