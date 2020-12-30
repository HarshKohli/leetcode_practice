# Author: Harsh Kohli
# Date created: 11/28/2020

def longestArithSeqLength(A):
    n = len(A)

    dp = [[0 for _ in range(n)] for _ in range(n)]
    answer = 0

    for j in range(1, n):

        index_map_2 = {}

        for i in range(j):
            diff = A[j] - A[i]
            prev = A[i] - diff
            if prev in index_map_2:
                prev_index = index_map_2[prev]
                sub_len = dp[prev_index][i] + 1
                dp[i][j] = sub_len
                if sub_len > answer:
                    answer = sub_len
            index_map_2[A[i]] = i

    return answer + 2


A = [22, 8, 57, 41, 36, 46, 42, 28, 42, 14, 9, 43, 27, 51, 0, 0, 38, 50, 31, 60, 29, 31, 20, 23, 37, 53, 27, 1, 47, 42,
     28, 31, 10, 35, 39, 12, 15, 6, 35, 31, 45, 21, 30, 19, 5, 5, 4, 18, 38, 51, 10, 7, 20, 38, 28, 53, 15, 55, 60, 56,
     43, 48, 34, 53, 54, 55, 14, 9, 56, 52]
print(longestArithSeqLength(A))
