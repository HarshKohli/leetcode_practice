# Author: Harsh Kohli
# Date created: 2/16/2021

def convert(s, numRows):
    rows = ['' for _ in range(numRows)]
    downwards = True
    ptr = 0
    for index, x in enumerate(s):
        rows[ptr] = rows[ptr] + x
        if downwards:
            ptr = ptr + 1
            if ptr == numRows:
                downwards = False
                ptr = ptr - 2
        else:
            ptr = ptr - 1
            if ptr < 0:
                downwards = True
                ptr = ptr + 2
    converted = ''.join(rows)
    return converted


s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))
