# Author: Harsh Kohli
# Date created: 10/26/2020

def divide(dividend, divisor):
    if divisor == 0:
        return 2147483647
    if dividend == 0:
        return 0
    is_neg = False
    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        is_neg = True
    if divisor < 0:
        divisor = 0 - divisor
    if dividend < 0:
        dividend = 0 - dividend

    values_dict = {}
    running_multiple = divisor
    values_dict[1] = (divisor, 1)
    multiple = 2
    step = 2
    while dividend >= running_multiple:
        running_multiple = running_multiple + running_multiple
        values_dict[step] = (running_multiple, multiple)
        multiple = multiple + multiple
        step = step + 1

    answer = 0
    step = step - 1
    while dividend >= divisor:
        to_subtract, multiple = values_dict[step]
        if to_subtract > dividend:
            step = step - 1
            continue
        dividend = dividend - to_subtract
        answer = answer + multiple

    if (is_neg and answer > 2147483648) or (not is_neg and answer > 2147483647):
        return 2147483647

    if is_neg:
        return 0 - answer
    return answer


print(divide(-2147483648, -3))
#print(divide(1173741824, 2))
