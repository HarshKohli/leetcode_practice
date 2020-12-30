# Author: Harsh Kohli
# Date created: 11/8/2020

def lenLongestFibSubseq(A):
    size = len(A)
    hashed = set()
    for num in A:
        hashed.add(num)

    max_len = 0
    for index, num in enumerate(A):
        if index > size - max_len:
            break
        for num2 in A[index + 1:]:
            count = 0
            first = num
            second = num2
            while (first + second) in hashed:
                count = count + 1
                temp = second
                second = first + second
                first = temp
            if count > max_len:
                max_len = count

    if max_len > 0:
        return max_len + 2
    return max_len


A = [2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50]
print(lenLongestFibSubseq(A))
