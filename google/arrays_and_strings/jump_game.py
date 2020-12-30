# Author: Harsh Kohli
# Date created: 8/3/2020

def canJump(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = 1
    for i in range(n):
        max_len = nums[i]
        if dp[i] == 1:
            for j in range(1, max_len + 1):
                if i + j < n:
                    dp[i + j] = 1
                if (i + j) == n - 1:
                    return True
    if dp[n-1] == 1:
        return True
    return dp[n-1]


def canJump2(nums):
    n = len(nums)
    latest_good = 0
    for i in range(n):
        if latest_good < i:
            return False
        if latest_good >= i and (i + nums[i]) > latest_good:
            latest_good = i + nums[i]
    if latest_good >= n-1:
        return True
    return False

nums = [0]
print(canJump2(nums))
