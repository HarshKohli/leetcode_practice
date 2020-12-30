# Author: Harsh Kohli
# Date created: 10/18/2020


def splitArray(nums, m):
    size = len(nums)
    if size == 1:
        return nums[0]
    largest_num = nums[0]
    sum = nums[0]
    for index in range(1, size):
        num = nums[index]
        if num > largest_num:
            largest_num = num
        sum = sum + largest_num
    l, r = largest_num, sum

    answer = sum
    while l <= r:
        mid = int((l + r) / 2)
        splits, running_sum, largest_sum = 1, 0, 0
        for index, num in enumerate(nums):
            if running_sum + num <= mid:
                running_sum = running_sum + num
                if index == size - 1:
                    if running_sum > largest_sum:
                        largest_sum = running_sum
            else:
                if running_sum > largest_sum:
                    largest_sum = running_sum
                running_sum = num
                splits = splits + 1
                if index == size - 1:
                    if running_sum > largest_sum:
                        largest_sum = running_sum
                if splits > m:
                    break

        if splits > m:
            l = mid + 1
        else:
            r = mid - 1
            if largest_sum < answer:
                answer = largest_sum
    return answer


nums = [1, 2, 3, 4, 5]
m = 2
print(splitArray(nums, m))
