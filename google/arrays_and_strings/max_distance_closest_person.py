# Author: Harsh Kohli
# Date created: 8/11/2020

def maxDistToClosest(seats):
    ptr = float('-inf')
    fwd_pass, back_pass = [], [0] * len(seats)
    for index, value in enumerate(seats):
        if value == 1:
            fwd_pass.append(0)
            ptr = index
        else:
            fwd_pass.append(index - ptr)

    ptr = float('inf')
    for index in range(len(seats) - 1, -1, -1):
        value = seats[index]
        if value == 1:
            back_pass[index] = 0
            ptr = index
        else:
            back_pass[index] = ptr - index

    max = 0
    for a, b in zip(fwd_pass, back_pass):
        distance = min(a, b)
        if distance > max:
            max = distance

    return max


input = [1, 0, 0, 0, 1, 0, 1]
dist = maxDistToClosest(input)
print(dist)
