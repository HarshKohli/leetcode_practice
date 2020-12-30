# Author: Harsh Kohli
# Date created: 9/5/2020

def trap(height):
    if len(height) == 0:
        return 0
    max_arr = [height[0]]
    for i, a in enumerate(height[1:]):
        if a > max_arr[i]:
            max_arr.append(a)
        else:
            max_arr.append(max_arr[i])
    size = len(height)
    max_arr_rev = [height[size - 1]]
    for i in range(size - 2, -1, -1):
        a = height[i]
        prev = max_arr_rev[-1]
        if a > prev:
            max_arr_rev.append(a)
        else:
            max_arr_rev.append(prev)
    max_arr_rev.reverse()
    sum = 0
    for i, h in enumerate(height):
        border = min(max_arr[i], max_arr_rev[i])
        sum = sum + (border - h)

    return sum


heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
vol = trap(heights)
print(vol)
