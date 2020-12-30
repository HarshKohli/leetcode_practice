# Author: Harsh Kohli
# Date created: 10/15/2020

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    dps = [0 for _ in range(256)]
    dpt = [0 for _ in range(256)]
    for a, b in zip(s, t):
        orda, ordb = ord(a), ord(b)
        dps[orda] = dps[orda] + 1
        dpt[ordb] = dpt[ordb] + 1
    if dps == dpt:
        return True
    return False


s = "anagram"
t = "nagaram"

is_anagram = isAnagram(s, t)
print(is_anagram)
