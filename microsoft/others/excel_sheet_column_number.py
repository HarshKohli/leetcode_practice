# Author: Harsh Kohli
# Date created: 11/23/2020

def titleToNumber(s):
    multiplier = 1
    sum = 0
    size = len(s)

    for index in range(size - 1, -1, -1):
        sum = sum + (ord(s[index]) - 64) * multiplier
        multiplier = multiplier * 26

    return sum


s = 'ZY'
print(titleToNumber(s))
