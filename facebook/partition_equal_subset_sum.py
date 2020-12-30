# Author: Harsh Kohli
# Date created: 12/4/2020

def canPartition(nums):
    total = 0
    for num in nums:
        total = total + num
    if total % 2 == 1:
        return False
    total = int(total / 2)
    dp = [0 for _ in range(total + 1)]
    for num in nums:
        for index in range(total, -1, -1):
            mark = dp[index]
            if mark == 1:
                next_index = index + num
                if next_index < total:
                    dp[next_index] = 1
                elif next_index == total:
                    return True
        if num < total:
            dp[num] = 1
        elif num == total:
            return True

    return False


nums = [1, 5, 11, 5]
print(canPartition(nums))
