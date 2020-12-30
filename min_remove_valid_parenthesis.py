# Author: Harsh Kohli
# Date created: 11/5/2020

def minRemoveToMakeValid(s):
    open, close = 0, 0
    final = ''
    for x in s:
        if x != '(' and x != ')':
            final = final + x
        elif x == '(':
            final = final + x
            open = open + 1
        elif x == ')':
            if close != open:
                final = final + x
                close = close + 1
    if open == close:
        return final
    else:
        diff = open - close
        new_final = ''
        for index in range(len(final) - 1, -1, -1):
            x = final[index]
            if x == '(' and diff > 0:
                diff = diff - 1
                continue
            new_final = new_final + x
        rev = ''
        for index in range(len(new_final) - 1, -1, -1):
            rev = rev + new_final[index]
        return rev


s = "lee(t(c)ode"
print(minRemoveToMakeValid(s))
