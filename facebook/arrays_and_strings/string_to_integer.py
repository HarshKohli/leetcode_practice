# Author: Harsh Kohli
# Date created: 10/20/2020


def myAtoi(s):
    if len(s) == 0:
        return 0
    x, index = s[0], 0
    while x == ' ':
        index = index + 1
        if index == len(s):
            return 0
        x = s[index]
    is_neg = False
    if x == '-':
        index = index + 1
        if index == len(s):
            return 0
        x = s[index]
        is_neg = True
    elif x == '+':
        index = index + 1
        if index == len(s):
            return 0
        x = s[index]
    value = ord(x)
    num_str = ''
    while 48 <= value <= 57:
        num_str = num_str + x
        index = index + 1
        num_int = int(num_str)
        if is_neg:
            num_int = 0 - num_int
        if num_int < (0 - 2 ** 31):
            return (0 - 2 ** 31)
        if num_int >= 2 ** 31:
            return 2 ** 31 - 1
        if index == len(s):
            break
        x = s[index]
        value = ord(x)
    if len(num_str) == 0:
        return 0
    else:
        unsigned = int(num_str)
        if is_neg:
            return (0 - unsigned)
        else:
            return unsigned


s = "42"
print(myAtoi(s))
