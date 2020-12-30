# Author: Harsh Kohli
# Date created: 7/27/2020

def lengthOfLongestSubstring(s):
    last_seen = {}
    start, max = 0, 0
    for end in range(len(s)):
        c = s[end]
        if c in last_seen:
            last = last_seen[c]
            last_seen[c] = end
            if last >= start:
                start = last + 1
            length = end - start + 1
            if length > max:
                max = length
        else:
            last_seen[c] = end
            length = end - start + 1
            if length > max:
                max = length
    return max


input = "bbbbb"
longest = lengthOfLongestSubstring(input)
print(longest)
