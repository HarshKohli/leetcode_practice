# Author: Harsh Kohli
# Date created: 11/7/2020

def kSmallestPairs(nums1, nums2, k):
    if len(nums1) == 0 or len(nums2) == 0:
        return []
    sums, pairs = [], []
    for num1 in nums1:
        for num2 in nums2:
            sums.append((num1 + num2, num1, num2))

    sums.sort()
    for index, triplet in enumerate(sums):
        if index == k:
            break
        pairs.append([triplet[1], triplet[2]])

    return pairs


nums1 = [1, 1, 2]
nums2 = [1, 2, 3]
k = 10
print(kSmallestPairs(nums1, nums2, k))
