# Author: Harsh Kohli
# Date created: 11/20/2020

def recurse(s, p, ptr1, ptr2, slen, plen, found_map):
    map_key = (ptr1, ptr2)
    if map_key in found_map:
        return found_map[map_key]

    if ptr1 == slen and ptr2 == plen:
        found_map[map_key] = True
        return True
    elif ptr1 == slen:
        while ptr2 < plen:
            if p[ptr2] != '*':
                found_map[map_key] = False
                return False
            ptr2 = ptr2 + 1
        found_map[map_key] = True
        return True
    elif ptr2 == plen:
        found_map[map_key] = False
        return False

    s_char = s[ptr1]
    p_char = p[ptr2]

    if p_char == '?':
        found = recurse(s, p, ptr1 + 1, ptr2 + 1, slen, plen, found_map)
        found_map[map_key] = found
        return found

    elif p_char == '*':
        jump = 0
        while ptr1 + jump <= slen:
            found = recurse(s, p, ptr1 + jump, ptr2 + 1, slen, plen, found_map)
            if found:
                found_map[map_key] = found
                return found
            jump = jump + 1
        found_map[map_key] = False
        return False

    else:
        if s_char == p_char:
            found = recurse(s, p, ptr1 + 1, ptr2 + 1, slen, plen, found_map)
            found_map[map_key] = found
            return found
        else:
            found_map[map_key] = False
            return False

def isMatch(s, p):
    s_len, p_len = len(s), len(p)
    p_copy = ''
    p_index = 0
    while p_index < p_len:
        val = p[p_index]
        p_copy = p_copy + val
        p_index = p_index + 1
        if val == '*':
            while p_index < p_len and p[p_index] == '*':
                p_index = p_index + 1

    return recurse(s, p_copy, 0, 0, s_len, len(p_copy), {})


s = "babbabbabaaaaabaabaaaaabbabaabbbaaaabbaabbbbbaabbabaabbbbaabbbabaabbaaabbbbabbbabbababaababbaaaaaabaabababbbaaabbaaaaaabbbabbbbabaabaaaabbabbaabaababbaaaababaaaaababbbaabaababbbaaabaababbabbabaaabbbbaa"
p = "*a*ab*b*ab*a*bb**bb**a**abb*bb*ab*a*bbbb***ba***aa**ba*b*ab*ba***aaabbbaa*ba*ba*b****baabb**b*aa*aaab*a"
print(isMatch(s, p))
