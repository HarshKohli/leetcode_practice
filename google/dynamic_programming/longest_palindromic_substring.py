# Author: Harsh Kohli
# Date created: 10/17/2020

def longestPalindrome(s):
    if len(s) == 1:
        return s
    if len(s) == 2:
        if s[0] == s[1]:
            return s
        else:
            return s[0]
    size = len(s)
    dp = [[0 for _ in range(size)] for _ in range(size)]
    for diag in range(size):
        dp[diag][diag] = 1
    max_i, max_j = 0, 0
    max_len = 1
    for index in range(size - 1):
        if s[index + 1] == s[index]:
            dp[index][index + 1] = 1
            max_i, max_j = index, index + 1
            max_len = 2
    for i in range(size - 1, -1, -1):
        for j in range(i + 2, size):
            if s[i] == s[j] and dp[i + 1][j - 1] == 1:
                dp[i][j] = 1
                length = j - i + 1
                if length > max_len:
                    max_len = length
                    max_i, max_j = i, j

    return s[max_i:max_j + 1]


s = "ccc"
longest_palin = longestPalindrome(s)
print(longest_palin)
