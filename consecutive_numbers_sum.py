# Author: Harsh Kohli
# Date created: 2/12/2021

def consecutiveNumbersSum(N):
    if N == 0:
        return 0
    count = 0
    running_sum = 0
    start = 1
    for index in range(1, N + 1):
        running_sum = running_sum + index
        if running_sum > N:
            while running_sum > N:
                running_sum = running_sum - start
                start = start + 1
        if running_sum == N:
            running_sum = running_sum - start
            start = start + 1
            count = count + 1
    return count

N = 1
print(consecutiveNumbersSum(N))
