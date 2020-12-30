# Author: Harsh Kohli
# Date created: 10/28/2020

def longestValidParentheses(s):
    stack = []
    max_len = 0
    stack.append(-1)
    for index, bracket in enumerate(s):
        print(stack)
        if bracket == '(':
            stack.append(index)
        else:
            prev = stack.pop()
            if len(stack) != 0:
                size = index - stack[-1]
                if size > max_len:
                    max_len = size
            else:
                stack.append(index)
    return max_len


s = "(((())))))))"
print(longestValidParentheses(s))
