# Author: Harsh Kohli
# Date created: 8/9/2020

def isValid(num, index, time_list):
    if index == 3:
        return True
    if index == 2 and num < 6:
        return True
    if index == 1 and num < 5:
        return True
    if index == 1 and time_list[0] < 2:
        return True
    if index == 0 and num < 3:
        return True
    return False


def nextClosestTime(time):
    broken = time.split(':')
    time_list = []
    for c in broken[0]:
        time_list.append(int(c))
    for c in broken[1]:
        time_list.append(int(c))

    next_time = []
    min_num = time_list[0]
    for num in time_list:
        if num < min_num:
            min_num = num
        next_time.append(num)

    found, replaced_index = False, -1
    for index in range(len(time_list) - 1, -1, -1):
        num, replacement = time_list[index], -1
        for index2, num2 in enumerate(time_list):
            if num2 > num and isValid(num2, index, time_list):
                if replacement == -1 or replacement > num2:
                    replacement = num2
        if replacement != -1:
            time_list[index] = replacement
            found = True
            replaced_index = index
            break

    if found:
        for index in range(replaced_index + 1, len(time_list)):
            time_list[index] = min_num
    else:
        for index in range(len(time_list)):
            time_list[index] = min_num

    final_time = ''
    for index, c in enumerate(time_list):
        final_time = final_time + str(c)
        if index == 1:
            final_time = final_time + ':'
    return final_time


time = "13:55"
next_time = nextClosestTime(time)
print(next_time)
