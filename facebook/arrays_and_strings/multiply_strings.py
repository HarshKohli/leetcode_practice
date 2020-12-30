# Author: Harsh Kohli
# Date created: 12/1/2020

def optim_mult(num1, num2):
    values_dict = {}
    multiplier = 1
    value = num1
    keys = []
    while multiplier <= num2:
        values_dict[multiplier] = value
        keys.append(multiplier)
        multiplier = multiplier + multiplier
        value = value + value

    index = len(keys) - 1
    answer = 0
    num2_copy = num2
    while num2_copy > 0:
        multiplier = keys[index]
        if multiplier <= num2_copy:
            answer = answer + values_dict[multiplier]
            num2_copy = num2_copy - multiplier
        index = index - 1

    return answer


def optim_div(num1, num2):
    values_dict = {}
    value = num2
    multiplier = 1
    keys = []
    while value <= num1:
        values_dict[multiplier] = value
        keys.append(multiplier)
        multiplier = multiplier + multiplier
        value = value + value

    num1_copy = num1
    div = 0
    index = len(keys) - 1
    #print('Num 1 ' + str(num1) + ' Num2 ' + str(num2))
    while num1_copy >= num2:
        print(index)
        multiplier = keys[index]
        value = values_dict[multiplier]
        if num1_copy >= value:
            div = div + multiplier
            num1_copy = num1_copy - value
        index = index - 1

    return div, num1_copy


def multiply(num1, num2):
    size1, size2 = len(num1), len(num2)
    if size1 == 0 or size2 == 0:
        return ''
    if size2 > size1:
        temp = size1
        size1 = size2
        size2 = temp
        temp = num1
        num1 = num2
        num2 = temp

    iter1 = 1
    ptr2 = size2 - 1
    sums = []
    while ptr2 >= 0:
        ptr1 = size1 - 1
        iter2 = 1
        minisum, carry = 0, 0
        digit2 = ord(num2[ptr2]) - 48
        while ptr1 >= 0:
            digit1 = ord(num1[ptr1]) - 48
            prod = optim_mult(digit1, digit2)
            prod = prod + carry
            div = 0
            while prod > 10:
                prod = prod - 10
                div = div + 1
            rem = prod
            minisum = minisum + optim_mult(iter2, rem)
            carry = div
            iter2 = optim_mult(iter2, 10)
            ptr1 = ptr1 - 1
        if carry > 0:
            minisum = minisum + optim_mult(carry, iter2)
        minisum = optim_mult(minisum, iter1)
        iter1 = optim_mult(iter1, 10)
        sums.append(minisum)
        ptr2 = ptr2 - 1

    answer = 0
    for one in sums:
        answer = answer + one

    if answer == 0:
        return '0'

    answer_str = ''
    prev = answer

    while prev > 0:
        div, rem = optim_div(prev, 10)
        answer_str = answer_str + chr(rem + 48)
        prev = div

    return answer_str[::-1]


num1 = '140'
num2 = '721'
print(multiply(num1, num2))
