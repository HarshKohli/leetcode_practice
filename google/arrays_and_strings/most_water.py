# Author: Harsh Kohli
# Date created: 7/27/2020


def maxArea(height):
    size = len(height)
    max = 0
    left, right = 0, size - 1
    while right > left:
        h1, h2 = height[left], height[right]
        min_height = min(h1, h2)
        area = min_height * (right - left)
        if area > max:
            max = area
        if min_height == h1:
            left = left + 1
        else:
            right = right - 1
    return max


input = [1, 8, 6, 2, 5, 4, 8, 3, 7]
max_area = maxArea(input)
print(max_area)
