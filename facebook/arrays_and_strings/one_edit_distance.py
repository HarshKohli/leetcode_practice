# Author: Harsh Kohli
# Date created: 10/21/2020

def isOneEditDistance(s, t):
    len1, len2 = len(s), len(t)
    if len2 > len1:
        if len2 - len1 > 1:
            return False
        edits = 0
        index2 = 0
        for index1, x in enumerate(s):
            y = t[index2]
            if x == y:
                index2 = index2 + 1
                continue
            if edits == 0:
                index2 = index2 + 1
                next_y = t[index2]
                if x != next_y:
                    return False
                index2 = index2 + 1
                edits = edits + 1
            elif edits == 1:
                return False
        return True

    elif len2 < len1:
        if len1 - len2 > 1:
            return False
        edits = 0
        index1 = 0
        for index2, y in enumerate(t):
            x = s[index1]
            if x == y:
                index1 = index1 + 1
                continue
            if edits == 0:
                index1 = index1 + 1
                next_x = s[index1]
                if y != next_x:
                    return False
                index1 = index1 + 1
                edits = edits + 1
            elif edits == 1:
                return False
        return True

    else:
        count = 0
        for x, y in zip(s, t):
            if x != y:
                count = count + 1
        if count == 1:
            return True
        else:
            return False


s = "teacher"
t = "tache"
print(isOneEditDistance(s, t))
