# Author: Harsh Kohli
# Date created: 10/20/2020

def merge(nums1, m, nums2, n):
    if n == 0:
        return
    if m == 0:
        for index in range(n):
            nums1[index] = nums2[index]
        return
    ptr1, ptr2 = m - 1, n - 1
    rev_ptr = len(nums1) - 1
    while ptr1 >= 0 and ptr2 >= 0:
        if nums1[ptr1] < nums2[ptr2]:
            nums1[rev_ptr] = nums2[ptr2]
            ptr2 = ptr2 - 1
        else:
            nums1[rev_ptr] = nums1[ptr1]
            ptr1 = ptr1 - 1
        rev_ptr = rev_ptr - 1

    for index in range(ptr2 + 1):
        nums1[index] = nums2[index]

nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
print(nums1)

