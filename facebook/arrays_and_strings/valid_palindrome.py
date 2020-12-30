# Author: Harsh Kohli
# Date created: 10/20/2020

def is_alpha_numeric(x):
    if 97 <= ord(x) <= 122:
        return True
    if 48 <= ord(x) <= 57:
        return True
    return False

def isPalindrome(s):
    size = len(s)
    lowered = s.lower()
    if size == 0:
        return True
    ptr1, ptr2 = 0, size - 1
    while ptr1 < ptr2:
        x, y = lowered[ptr1], lowered[ptr2]
        if not is_alpha_numeric(x):
            ptr1 = ptr1 + 1
            continue
        if not is_alpha_numeric(y):
            ptr2 = ptr2 - 1
            continue
        if x != y:
            return False
        ptr1 = ptr1 + 1
        ptr2 = ptr2 - 1
    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
