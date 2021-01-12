# Author: Harsh Kohli
# Date created: 1/12/2021

def kEmptySlots(bulbs, k):
    size = len(bulbs)
    if size == 0:
        return -1

    dayswitchedon = [0 for _ in range(size + 1)]
    for day, bulb in enumerate(bulbs):
        dayswitchedon[bulb] = day + 1

    left, right = 1, k + 2

    ans = float('inf')
    while right <= size:
        a, b = dayswitchedon[left], dayswitchedon[right]
        not_ans = False
        for index in range(left + 1, right):
            c = dayswitchedon[index]
            if c > a and c > b:
                continue
            not_ans = True
            break
        if not_ans:
            left = index
            right = left + k + 1
        else:
            day_num = max(a, b)
            if day_num < ans:
                ans = day_num
            left = right
            right = left + k + 1
    if ans != float('inf'):
        return ans
    return -1


bulbs = [3, 9, 2, 8, 1, 6, 10, 5, 4, 7]
k = 1
print(kEmptySlots(bulbs, k))
