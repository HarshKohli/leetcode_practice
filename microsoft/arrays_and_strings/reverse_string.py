# Author: Harsh Kohli
# Date created: 11/17/2020

def reverseString(s):
    size = len(s)
    for i in range(int(size / 2)):
        temp = s[size - i - 1]
        s[size - i - 1] = s[i]
        s[i] = temp


s = ["h", "e", "l", "l", "o"]
reverseString(s)
print(s)
