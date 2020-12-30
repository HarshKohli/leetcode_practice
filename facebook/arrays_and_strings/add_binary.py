# Author: Harsh Kohli
# Date created: 10/20/2020

def addBinary(a, b):
    if len(b) > len(a):
        y = b
        x = a
    else:
        y = a
        x = b
    a_index = len(x) - 1
    sum = ''
    carry = 0
    for index in range(len(y) - 1, -1, -1):
        b_digit = y[index]
        minisum = 0
        if b_digit == '1':
            minisum = minisum + 1
        if carry == 1:
            minisum = minisum + 1
        if a_index >= 0:
            a_digit = x[a_index]
            if a_digit == '1':
                minisum = minisum + 1
            a_index = a_index - 1
        if minisum == 3:
            sum = sum + '1'
            carry = 1
        elif minisum == 2:
            sum = sum + '0'
            carry = 1
        elif minisum == 1:
            sum = sum + '1'
            carry = 0
        else:
            sum = sum + '0'
            carry = 0
    if carry == 1:
        sum = sum + '1'
    return sum[::-1]


a = "11"
b = "1"
print(addBinary(a, b))
