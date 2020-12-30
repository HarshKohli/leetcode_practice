# Author: Harsh Kohli
# Date created: 11/5/2020

def checkInclusion(s1, s2):
    dp = [0 for _ in range(26)]
    for x in s1:
        index = ord(x) - 97
        dp[index] = dp[index] + 1

    sdp = [0 for _ in range(26)]
    p_len = len(s1)
    for x in s2[:p_len]:
        index = ord(x) - 97
        sdp[index] = sdp[index] + 1

    if dp == sdp:
        return True

    for index in range(1, len(s2)):
        end_index = index + len(s1) - 1
        if end_index >= len(s2):
            break
        to_remove = ord(s2[index - 1]) - 97
        to_add = ord(s2[end_index]) - 97
        sdp[to_remove] = sdp[to_remove] - 1
        sdp[to_add] = sdp[to_add] + 1
        if dp == sdp:
            return True

    return False


s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))

