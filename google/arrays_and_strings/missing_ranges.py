# Author: Harsh Kohli
# Date created: 8/9/2020

def findMissingRanges(nums, lower, upper):
    ranges = []
    for index, num in enumerate(nums):
        if index > 0:
            if num != nums[index - 1] + 1:
                small = max(nums[index - 1] + 1, lower)
                big = min(num - 1, upper)
                if big > small:
                    ranges.append(str(small) + '->' + str(big))
                elif big == small:
                    ranges.append(str(small))
        else:
            if lower < num:
                if lower == num - 1:
                    ranges.append(str(lower))
                else:
                    ranges.append(str(lower) + '->' + str(num - 1))
    if len(nums) > 0:
        if nums[-1] < upper:
            if nums[-1] == upper - 1:
                ranges.append(str(upper))
            else:
                ranges.append(str(nums[-1] + 1) + '->' + str(upper))
    else:
        if lower != upper:
            ranges.append(str(lower) + '->' + str(upper))
        else:
            ranges.append(str(lower))
    return ranges


nums = [0, 1, 3, 50, 75]
output = findMissingRanges(nums, 0, 99)
print(output)
