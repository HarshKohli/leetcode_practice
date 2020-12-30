# Author: Harsh Kohli
# Date created: 11/7/2020

def isSubsequence(s, t):
    ptr = 0
    if len(s) == 0:
        return True
    if len(t) == 0:
        return False
    for x in t:
        if x == s[ptr]:
            ptr = ptr + 1
        if ptr == len(s):
            return True

    return False


s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))
