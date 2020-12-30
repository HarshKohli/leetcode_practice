# Author: Harsh Kohli
# Date created: 10/28/2020

def intersect(nums1, nums2):
    unique1, unique2 = {}, {}

    for num in nums1:
        if num in unique1:
            unique1[num] = unique1[num] + 1
        else:
            unique1[num] = 1

    for num in nums2:
        if num in unique2:
            unique2[num] = unique2[num] + 1
        else:
            unique2[num] = 1

    intersection = []

    for num, count1 in unique1.items():
        if num in unique2:
            count2 = unique2[num]
            inter_count = min(count1, count2)
            for _ in range(inter_count):
                intersection.append(num)

    return intersection


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))
