# Author: Harsh Kohli
# Date created: 7/23/2020

import time


def oddEvenJumps(A):
    n = len(A)
    valid_pos = [0] * n
    odd_jumps = [-1] * n
    even_jumps = [-1] * n

    odd_jumps[n - 1] = n - 1
    even_jumps[n - 1] = n - 1
    valid_pos[n-1] = 1

    stack = []
    pos_a = [(y, x) for x, y in enumerate(A)]
    pos_a.sort()

    for num, index in pos_a:
        while len(stack) > 0 and stack[-1] < index:
            head = stack.pop()
            odd_jumps[head] = index
        stack.append(index)

    stack = []
    pos_a = [(-y, x) for x, y in enumerate(A)]
    pos_a.sort()

    for num, index in pos_a:
        while len(stack) > 0 and stack[-1] < index:
            head = stack.pop()
            even_jumps[head] = index
        stack.append(index)

    count = 1
    for index in range(n-2, -1, -1):
        next_pos = odd_jumps[index]
        if next_pos == -1:
            continue
        elif next_pos == n-1:
            valid_pos[index] = 1
            count = count + 1
            continue
        else:
            next_pos = even_jumps[next_pos]
            if next_pos != -1 and valid_pos[next_pos] == 1:
                valid_pos[index] = 1
                count = count + 1

    return count


input = [10, 13, 12, 14, 15]
start = time.time()
pos_jumps = oddEvenJumps(input)
time_taken = time.time() - start
print('Time taken ' + str(time_taken))
#print(len(input))
print(pos_jumps)
