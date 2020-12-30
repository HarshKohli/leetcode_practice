# Author: Harsh Kohli
# Date created: 9/11/2020

def backspaceCompare(S, T):
    stack1, stack2 = [], []
    for x in S:
        if x == '#':
            size = len(stack1)
            if size > 0:
                stack1.pop(size - 1)
        else:
            stack1.append(x)

    for x in T:
        if x == '#':
            size = len(stack2)
            if size > 0:
                stack2.pop(size - 1)
        else:
            stack2.append(x)

    if len(stack1) != len(stack2):
        return False
    for x, y in zip(stack1, stack2):
        if x != y:
            return False

    return True


S = "ab#c"
T = "ad#c"
is_same = backspaceCompare(S, T)
print(is_same)
