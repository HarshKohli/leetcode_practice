# Author: Harsh Kohli
# Date created: 8/8/2020

def lengthOfLongestSubstringTwoDistinct(s):
    ptr1, ptr2 = 0, 0
    two_dist = []
    max_len = 0
    size = len(s)
    final_flip = False
    for index, c in enumerate(s):
        if len(two_dist) < 2:
            if c not in two_dist:
                two_dist.append(c)
            if index > 0 and c != s[index - 1]:
                ptr2 = index
            continue
        if c in two_dist:
            if c != s[index - 1]:
                ptr2 = index
            continue
        if c not in two_dist:
            length = index - ptr1
            if length > max_len:
                max_len = length
            ptr1 = ptr2
            ptr2 = index
            if index == size - 1:
                final_flip = True
            two_dist = [s[index - 1], s[index]]

    if not final_flip:
        length = size - ptr1
        if length > max_len:
            max_len = length
    return max_len


input = "eceba"
length = lengthOfLongestSubstringTwoDistinct(input)
print(length)
