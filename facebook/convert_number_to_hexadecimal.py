# Author: Harsh Kohli
# Date created: 11/29/2020

def toHex(num):
    if num < 0:
        num = num + 2**32
    elif num == 0:
        return '0'

    answer = ''
    while num > 0:
        digit = num % 16
        num = int(num /16)
        if digit < 10:
            answer = answer + str(digit)
        else:
            answer = answer + chr(97 + digit - 10)

    return answer[::-1]


num = 0
print(toHex(num))
