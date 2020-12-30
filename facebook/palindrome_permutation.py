# Author: Harsh Kohli
# Date created: 12/3/2020

def canPermutePalindrome(s):
    count_map = {}
    for x in s:
        if x in count_map:
            count_map[x] = count_map[x] + 1
        else:
            count_map[x] = 1

    size = len(s)
    is_odd = False
    if size % 2 == 1:
        is_odd = True

    odd_count = 0
    for _, count in count_map.items():
        if count % 2 == 1:
            odd_count = odd_count + 1
            if is_odd and odd_count > 1:
                return False
            if not is_odd:
                return False
    return True


s = "aab"
print(canPermutePalindrome(s))
