# Author: Harsh Kohli
# Date created: 11/7/2020

def countAndSay(n):
    if n == 0:
        return ''
    prev = '1'
    for _ in range(n - 1):
        index = 0
        new_prev = ''
        while index < len(prev):
            count = 0
            prev_letter = prev[index]
            while prev[index] == prev_letter:
                count = count + 1
                index = index + 1
                if index == len(prev):
                    break
            new_prev = new_prev + str(count) + prev_letter
        prev = new_prev
    return prev


n = 4
print(countAndSay(n))
