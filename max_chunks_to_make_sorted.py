# Author: Harsh Kohli
# Date created: 11/5/2020

def maxChunksToSorted(arr):
    max, chunks = 0, 0
    for index, num in enumerate(arr):
        if num > max:
            max = num
        if max == index:
            chunks = chunks + 1
    return chunks

arr = [1,0,2,3,4]
print(maxChunksToSorted(arr))

