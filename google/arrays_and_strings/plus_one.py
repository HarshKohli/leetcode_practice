# Author: Harsh Kohli
# Date created: 8/3/2020

def plusOne(digits):
    i = len(digits) - 1
    while i > 0 and digits[i] == 9:
        digits[i] = 0
        i = i - 1
    if i > 0:
        digits[i] = digits[i] + 1
    else:
        if digits[i] == 9:
            digits[i] = 1
            digits.append(0)
        else:
            digits[i] = digits[i] + 1
    return digits


digits = [9, 1, 9, 9]
next = plusOne(digits)
print(next)
