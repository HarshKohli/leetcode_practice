# Author: Harsh Kohli
# Date created: 10/22/2020

def validPalindrome(s):
    ptr1, ptr2 = 0, len(s) - 1
    count = 0
    redo = False
    while ptr1 < ptr2:
        x, y = s[ptr1], s[ptr2]
        if x == y:
            ptr1 = ptr1 + 1
            ptr2 = ptr2 - 1
            continue
        else:
            if ptr2 - ptr1 == 1:
                count = count + 1
                break
            else:
                if count == 0:
                    left, right = ptr1 + 1, ptr2
                ptr2 = ptr2 - 1
                count = count + 1
                redo = True
    if count < 2:
        return True
    else:
        if redo:
            ptr1, ptr2 = left, right
            while ptr1 < ptr2:
                x, y = s[ptr1], s[ptr2]
                if x == y:
                    ptr1 = ptr1 + 1
                    ptr2 = ptr2 - 1
                    continue
                else:
                    return False
            return True
        return False


s = 'tcaac'
print(validPalindrome(s))
