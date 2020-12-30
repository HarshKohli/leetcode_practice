# Author: Harsh Kohli
# Date created: 11/7/2020

def is_valid(num, mirror):
    x = num
    while x > 0:
        digit = x % 10
        if digit in mirror:
            return True
        x = int(x / 10)
    return False


def recurse(num, N, same, mirror):
    if num > N:
        return 0
    count = 0
    if is_valid(num, mirror):
        count = count + 1
    for digit in same:
        x = 10 * num + digit
        count = count + recurse(x, N, same, mirror)
    for digit in mirror:
        x = 10 * num + digit
        count = count + recurse(x, N, same, mirror)
    return count


def rotatedDigits(N):
    same = [0, 1, 8]
    mirror = [2, 5, 6, 9]
    count = 0
    for x in same[1:]:
        count = count + recurse(x, N, same, mirror)
    for x in mirror:
        count = count + recurse(x, N, same, mirror)
    return count


n = 20
print(rotatedDigits(n))
