# Author: Harsh Kohli
# Date created: 11/24/2020


def count_subarrays(arr):
    stack = []
    start, end = [0 for _ in range(len(arr))], [0 for _ in range(len(arr))]

    stack.append((arr[0], 1, 0))
    for index in range(1, len(arr)):
        num = arr[index]
        count = 1
        while len(stack) > 0 and stack[-1][0] < num:
            prev, prev_count, prev_index = stack.pop()
            count = count + prev_count
            start[prev_index] = prev_count

        stack.append((num, count, index))

    for num, count, index in stack:
        start[index] = count

    stack = []
    stack.append((arr[-1], 1, len(arr) - 1))

    for index in range(len(arr) - 2, -1, -1):
        num = arr[index]
        count = 1
        while len(stack) > 0 and stack[-1][0] < num:
            prev, prev_count, prev_index = stack.pop()
            count = count + prev_count
            end[prev_index] = prev_count

        stack.append((num, count, index))

    for num, count, index in stack:
        end[index] = count

    answer = []
    for num1, num2 in zip(start, end):
        answer.append(num1 + num2 - 1)

    return answer


arr = [3, 4, 1, 6, 2]
print(count_subarrays(arr))
