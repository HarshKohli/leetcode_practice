# Author: Harsh Kohli
# Date created: 11/24/2020

def canBeEqual(target, arr):
    count_dict = {}
    if len(target) != len(arr):
        return False
    for num in arr:
        if num in count_dict:
            count_dict[num] = count_dict[num] + 1
        else:
            count_dict[num] = 1

    for num in target:
        if num not in count_dict:
            return False
        count_dict[num] = count_dict[num] - 1

    for _, value in count_dict.items():
        if value != 0:
            return False

    return True


target = [1, 2, 3, 4]
arr = [2, 4, 1, 3]
print(canBeEqual(target, arr))
