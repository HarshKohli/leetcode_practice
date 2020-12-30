# Author: Harsh Kohli
# Date created: 10/19/2020


def canTransform(start, end):
    l1, l2, r1, r2 = 0, 0, 0, 0
    trimmed1, trimmed2 = '', ''
    for x, y in zip(start, end):
        if x == 'L':
            l1 = l1 + 1
            trimmed1 = trimmed1 + x
        if y == 'L':
            l2 = l2 + 1
            trimmed2 = trimmed2 + y
        if x == 'R':
            r1 = r1 + 1
            trimmed1 = trimmed1 + x
        if y == 'R':
            r2 = r2 + 1
            trimmed2 = trimmed2 + y
        if l1 > l2:
            return False
        if r1 < r2:
            return False
    if trimmed1 == trimmed2:
        return True
    return False



start = "RXXLRXRXL"
end = "XRLXXRRLX"

# start = "XXXXXLXXXX"
# end = "LXXXXXXXXX"

print(canTransform(start, end))
