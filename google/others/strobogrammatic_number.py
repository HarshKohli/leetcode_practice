# Author: Harsh Kohli
# Date created: 10/19/2020

def isStrobogrammatic(num):
    size = len(num)
    if size == 0:
        return True
    left, right = 0, size - 1
    while left <= right:
        x, y = num[left], num[right]
        if x not in ['0', '1', '6', '8', '9'] or y not in ['0', '1', '6', '8', '9']:
            return False
        if left == right:
            if x not in ['0', '1', '8']:
                return False
            else:
                break
        if x in ['0', '1', '8']:
            if y != x:
                return False
        if x == '6' and y != '9':
            return False
        if x == '9' and y != '6':
            return False
        left = left + 1
        right = right - 1

    return True


num = "88"
print(isStrobogrammatic(num))
