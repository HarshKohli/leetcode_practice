# Author: Harsh Kohli
# Date created: 10/21/2020

digits_map = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
two_digits_map = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
                  17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty',
                  6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}


def threeDigitToWords(three):
    small = ''
    hundreds = int(three / 100)
    if hundreds > 0:
        small = small + digits_map[hundreds] + ' Hundred '
    two = three % 100
    if two in two_digits_map and two >= 10:
        small = small + two_digits_map[two] + ' '
    else:
        tens = int(two / 10)
        if tens > 0:
            small = small + two_digits_map[tens] + ' '
        ones = two % 10
        if ones > 0:
            small = small + digits_map[ones] + ' '
    return small.strip()


def numberToWords(num):
    if num == 0:
        return 'Zero'
    words = ''
    billions = int(num / 10 ** 9)
    if billions > 0:
        words = words + threeDigitToWords(billions) + ' Billion '
    left = num % (10 ** 9)
    millions = int(left / 10 ** 6)
    if millions > 0:
        words = words + threeDigitToWords(millions) + ' Million '
    left = num % (10 ** 6)
    thousands = int(left/1000)
    if thousands > 0:
        words = words + threeDigitToWords(thousands) + ' Thousand '

    last_three = num % 1000
    if last_three > 0:
        words = words + threeDigitToWords(last_three)

    return words.strip()


num = 5
print(numberToWords(num))

