# Author: Harsh Kohli
# Date created: 10/1/2020

from queue import LifoQueue

def decodeString(s):
    stack = LifoQueue()
    for char in s:
        if char != ']':
            stack.put(char)
        else:
            present_str = ''
            new_char = stack.get()
            while new_char != '[':
                present_str = present_str + new_char
                new_char = stack.get()
            # reverse
            present_str = present_str[::-1]
            multiple = stack.get()
            if not stack.empty():
                next_digit = stack.get()
                while '0' <= next_digit <= '9':
                    multiple = multiple + next_digit
                    if stack.empty():
                        break
                    next_digit = stack.get()
                if next_digit > '9' or next_digit < '0':
                    stack.put(next_digit)
                #stack.put(next_digit)
            multiple = multiple[::-1]
            multiple = int(multiple)
            for _ in range(multiple):
                for a in present_str:
                    stack.put(a)
    answer = ''
    while not stack.empty():
        answer = answer + stack.get()
    return answer[::-1]

s = "3[a]2[bc]"
print(decodeString(s))
