# Author: Harsh Kohli
# Date created: 11/17/2020

def reverseWords(s):
    size = len(s)
    for i in range(int(size / 2)):
        temp = s[size - 1 - i]
        s[size - 1 - i] = s[i]
        s[i] = temp

    index = 0
    while index < size:
        start = index
        end = index
        while end < size and s[end] != ' ':
            end = end + 1
        end = end - 1
        word_size = end - start + 1
        for i in range(int(word_size / 2)):
            temp = s[end - i]
            s[end - i] = s[start + i]
            s[start + i] = temp
        index = end + 2


s = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
reverseWords(s)
print(s)
