# Author: Harsh Kohli
# Date created: 1/16/2021

def repeatedStringMatch(a, b):
    size1, size2 = len(a), len(b)
    reps, rem = int(size2 / size1), size2 % size1
    if rem > 0:
        reps = reps + 1

    final = ''
    for _ in range(reps):
        final = final + a

    if b in final:
        return reps

    final = final + a
    if b in final:
        return reps + 1

    return -1


a = "abcd"
b = "cdabcdab"
print(repeatedStringMatch(a, b))
