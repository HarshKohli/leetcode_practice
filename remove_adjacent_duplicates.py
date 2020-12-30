# Author: Harsh Kohli
# Date created: 12/5/2020

def removeDuplicates(s, k):
    stack = []
    for x in s:
        if len(stack) == 0:
            stack.append((x, 1))
        else:
            letter, count = stack[-1]
            if letter == x:
                if count == k - 1:
                    for _ in range(k - 1):
                        stack.pop()
                else:
                    stack.append((x, count + 1))
            else:
                stack.append((x, 1))

    ans = ''
    for x in stack:
        ans = ans + x[0]

    return ans


s = "pbbcggttciiippooaais"
k = 2
print(removeDuplicates(s, k))
