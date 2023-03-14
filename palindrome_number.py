def isPalindrome(x):
    if x < 0:
        return False
    new_num = 0
    new_x = x
    while new_x > 0:
        digit = new_x % 10
        new_x = int(new_x/10)
        if new_num == 0:
            new_num = digit
        else:
            new_num = new_num * 10 + digit
    if new_num != x:
        return False
    return True

x = 1231
print(isPalindrome(x))
