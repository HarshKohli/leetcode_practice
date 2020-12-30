# Author: Harsh Kohli
# Date created: 8/4/2020

def check_if_valid(target, char_to_occurence):
    for x, count in target.items():
        if x not in char_to_occurence:
            return False
        count2 = char_to_occurence[x]
        if count2 < count:
            return False
    return True


def minWindow(s, t):
    min_len, min_start = float('inf'), -1
    char_to_occurence, target = {}, {}
    for x in t:
        if x in target:
            target[x] = target[x] + 1
        else:
            target[x] = 1
    indices = []
    for index, x in enumerate(s):
        if x in t:
            indices.append(index)
            if x in char_to_occurence:
                char_to_occurence[x] = char_to_occurence[x] + 1
            else:
                char_to_occurence[x] = 1
            start = -1
            while check_if_valid(target, char_to_occurence):
                start = indices.pop(0)
                char_to_occurence[s[start]] = char_to_occurence[s[start]] - 1
            if start != -1:
                length = index - start + 1
                if length < min_len:
                    min_len = length
                    min_start = start
    if min_start == -1:
        return ""
    else:
        return s[min_start: min_start + min_len]


S = "cabwefgewcwaefgcf"
T = "cae"
min_substring = minWindow(S, T)
print(min_substring)
