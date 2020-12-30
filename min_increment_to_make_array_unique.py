# Author: Harsh Kohli
# Date created: 11/7/2020

def minIncrementForUnique(A):
    dp = [0 for _ in range(400001)]
    for num in A:
        dp[num] = dp[num] + 1
    incs = 0
    prev_non_zero = 1
    for index in range(len(dp)):
        while dp[index] > 1:
            for ptr in range(max(index, prev_non_zero), len(dp)):
                if dp[ptr] == 0:
                    dp[ptr] = 1
                    prev_non_zero = ptr
                    incs = incs + ptr - index
                    break
            dp[index] = dp[index] - 1
    return incs


A = [0, 2, 2]
print(minIncrementForUnique(A))
