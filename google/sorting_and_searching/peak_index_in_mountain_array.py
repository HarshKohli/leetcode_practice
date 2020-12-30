# Author: Harsh Kohli
# Date created: 10/17/2020

def peakIndexInMountainArray(arr):
    left, right = 1, len(arr) - 1
    while True:
        mid = int((left + right) / 2)
        l, r, m = arr[mid - 1], arr[mid + 1], arr[mid]
        if l < m and r < m:
            return mid
        else:
            if m > l:
                left = mid + 1
            else:
                right = mid - 1


arr = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
peak = peakIndexInMountainArray(arr)
print(peak)
