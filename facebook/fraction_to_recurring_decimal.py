# Author: Harsh Kohli
# Date created: 11/30/2020

def fractionToDecimal(numerator, denominator):
    is_negative = False
    if numerator > 0 and denominator < 0:
        denominator = 0 - denominator
        is_negative = True
    if numerator < 0 and denominator > 0:
        numerator = 0 - numerator
        is_negative = True

    if numerator < 0 and denominator < 0:
        numerator = 0 - numerator
        denominator = 0 - denominator

    decimal = str(int(numerator / denominator))
    remainder = numerator % denominator
    fraction = ''

    remainder = remainder * 10

    index = 0

    seen_dict = {}
    is_recurring = False

    while remainder > 0:
        a = int(remainder / denominator)
        fraction = fraction + str(a)
        b = remainder % denominator
        if remainder in seen_dict:
            is_recurring = True
            start = seen_dict[remainder]
            end = index
            break
        seen_dict[remainder] = index
        remainder = b * 10
        index = index + 1

    if fraction != '':
        if is_recurring:
            recurring_part = fraction[start:end]
            fraction = fraction[:start] + '(' + recurring_part + ')'
        answer = decimal + '.' + fraction
    else:
        answer = decimal

    if is_negative:
        answer = '-' + answer

    return answer


numerator = -1
denominator = -2147483648
print(fractionToDecimal(numerator, denominator))
