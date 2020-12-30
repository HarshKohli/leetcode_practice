# Author: Harsh Kohli
# Date created: 11/4/2020

def findAnagrams(s, p):
    dp = [0 for _ in range(26)]
    for x in p:
        index = ord(x) - 97
        dp[index] = dp[index] + 1

    sdp = [0 for _ in range(26)]
    p_len = len(p)
    for x in s[:p_len]:
        index = ord(x) - 97
        sdp[index] = sdp[index] + 1

    ana_indices = []
    if dp == sdp:
        ana_indices.append(0)

    for index in range(1, len(s)):
        end_index = index + len(p) - 1
        if end_index >= len(s):
            break
        to_remove = ord(s[index - 1]) - 97
        to_add = ord(s[end_index]) - 97
        sdp[to_remove] = sdp[to_remove] - 1
        sdp[to_add] = sdp[to_add] + 1
        if dp == sdp:
            ana_indices.append(index)

    return ana_indices


s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))
