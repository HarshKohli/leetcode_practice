# Author: Harsh Kohli
# Date created: 10/19/2020

def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    mapping, reverse_mapping = {}, {}
    for x, y in zip(s, t):
        if x in mapping:
            if mapping[x] != y:
                return False
        elif y in reverse_mapping:
            if reverse_mapping[y] != x:
                return False
        else:
            mapping[x] = y
            reverse_mapping[y] = x
    return True


s = "paper"
t = "title"
print(isIsomorphic(s, t))
