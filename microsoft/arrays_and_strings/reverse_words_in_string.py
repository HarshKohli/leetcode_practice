# Author: Harsh Kohli
# Date created: 11/17/2020

def reverseWords(s):
    size = len(s)
    final = ''
    if size == 0:
        return final

    index = size - 1
    while index >= 0:
        letter = s[index]
        while letter == ' ' and index >= 0:
            index = index - 1
            letter = s[index]
        rev_word = ''
        while index >= 0 and letter != ' ':
            rev_word = rev_word + letter
            index = index - 1
            letter = s[index]
        for x in rev_word[::-1]:
            final = final + x

        final = final + ' '

    return final.strip()


s = " a good   example        "
print(reverseWords(s))
