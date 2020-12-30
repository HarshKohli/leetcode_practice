# Author: Harsh Kohli
# Date created: 10/21/2020

def lengthOfLongestSubstringKDistinct(s, k):
    if k == 0:
        return 0
    occurence_map = {}
    start = 0
    longest, present = '', ''
    for i, x in enumerate(s):
        if x not in occurence_map:
            if len(occurence_map) < k:
                occurence_map[x] = 1
                present = present + x
                continue
            else:
                if len(present) > len(longest):
                    longest = present
                while len(occurence_map) >= k:
                    to_remove = s[start]
                    occurence_map[to_remove] = occurence_map[to_remove] - 1
                    if occurence_map[to_remove] == 0:
                        occurence_map.pop(to_remove)
                    start = start + 1
                present = s[start: i + 1]
                occurence_map[x] = 1
        else:
            present = present + x
            occurence_map[x] = occurence_map[x] + 1

    if len(present) > len(longest):
        longest = present

    return len(longest)


s = "aba"
k = 1
print(lengthOfLongestSubstringKDistinct(s, k))
