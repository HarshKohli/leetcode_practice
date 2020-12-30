# Author: Harsh Kohli
# Date created: 10/18/2020


def reverse(x):
    if x < 0:
        num = 0 - x
        is_neg = True
    else:
        num = x
        is_neg = False

    new_num_arr = []
    while num > 0:
        digit = num % 10
        new_num_arr.append(digit)
        num = int(num / 10)

    new_num = 0
    multiplier = 1
    for index in range(len(new_num_arr) - 1, -1, -1):
        digit = new_num_arr[index]
        new_num = new_num + digit * multiplier
        multiplier = multiplier * 10

    if is_neg:
        new_num = 0 - new_num

    if new_num < -2 ** 31 or new_num > 2 ** 31:
        return 0

    return new_num


x = -321
rev = reverse(x)
print(rev)
