# Author: Harsh Kohli
# Date created: 11/8/2020

def largestRectangleArea_slow(heights):
    size = len(heights)
    if size == 0:
        return 0

    max_height = 0
    for index, num in enumerate(heights):
        count = 1
        for num2 in heights[index + 1:]:
            if num2 < num:
                break
            count = count + 1
        for ptr in range(index - 1, -1, -1):
            num2 = heights[ptr]
            if num2 < num:
                break
            count = count + 1
        height = num * count
        if height > max_height:
            max_height = height

    return max_height


def largestRectangleArea(heights):
    heights.append(0)
    size = len(heights)
    if size == 0:
        return 0
    stack = []
    stack.append((0, heights[0]))
    index = 1
    max_area = 0

    while index < size:
        num = heights[index]
        new_index = float('inf')
        if num > max_area:
            max_area = num
        while len(stack) > 0:
            pos, height = stack[-1]
            if height > num:
                stack.pop()
                new_index = pos
                area = height * (index - pos)
                if area > max_area:
                    max_area = area
            else:
                break
        new_index = min(new_index, index)
        stack.append((new_index, num))
        index = index + 1

    return max_area


heights = [2, 1, 2]
print(largestRectangleArea(heights))
