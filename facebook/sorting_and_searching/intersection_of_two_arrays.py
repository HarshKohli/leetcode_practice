# Author: Harsh Kohli
# Date created: 10/28/2020

def intersection(nums1, nums2):
    unique = set()
    for num in nums1:
        unique.add(num)
    inter = set()
    for num in nums2:
        if num in unique:
            inter.add(num)
    return list(inter)


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2))
