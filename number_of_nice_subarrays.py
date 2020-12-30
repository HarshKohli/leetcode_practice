# Author: Harsh Kohli
# Date created: 12/6/2020

def numberOfSubarrays(nums, k):
    num_odd, start = 0, 0
    count = 0
    found = False
    for index, num in enumerate(nums):
        if num % 2 == 1:
            num_odd = num_odd + 1
            if num_odd == k:
                found = True
                prev_sum = 0
                while nums[start] % 2 != 1:
                    prev_sum = prev_sum + 1
                    start = start + 1
                prev_sum = prev_sum + 1
                count = count + prev_sum
                start = start + 1
                num_odd = num_odd - 1
        elif found:
            count = count + prev_sum

    return count


nums = [1, 1, 2, 1, 1]
k = 3
print(numberOfSubarrays(nums, k))
