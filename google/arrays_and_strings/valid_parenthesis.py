# Author: Harsh Kohli
# Date created: 8/12/2020

def isValid(s):
    stack = []
    closing_map = {}
    closing_map['('] = ')'
    closing_map['{'] = '}'
    closing_map['['] = ']'

    for bracket in s:
        if len(stack) > 0 and stack[-1] in closing_map and bracket == closing_map[stack[-1]]:
            stack.pop(len(stack) - 1)
        else:
            stack.append(bracket)
    if len(stack) > 0:
        return False
    else:
        return True


input = "{[]}"
print(isValid(input))
