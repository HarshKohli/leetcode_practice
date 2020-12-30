# Author: Harsh Kohli
# Date created: 11/5/2020

def addStrings(num1, num2):
    len1, len2 = len(num1), len(num2)
    size = max(len1, len2)
    carry = 0
    answer = ''
    for index in range(size):
        ind1, ind2 = len1 - index - 1, len2 - index - 1
        if ind1 >= 0:
            a = ord(num1[ind1]) - 48
        else:
            a = 0
        if ind2 >= 0:
            b = ord(num2[ind2]) - 48
        else:
            b = 0
        part = a + b + carry
        answer = answer + str(part % 10)
        carry = int(part / 10)

    if carry != 0:
        answer = answer + str(carry)
    return answer[::-1]


num1 = '91'
num2 = '9999'
print(addStrings(num1, num2))
