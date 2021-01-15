# Author: Harsh Kohli
# Date created: 1/15/2021

def get_rots(nums1, nums2, target):
    flips = 0
    for num1, num2 in zip(nums1, nums2):
        if num1 == target:
            continue
        if num2 == target:
            flips = flips + 1
            continue
        return float('inf')
    return flips


def minDominoRotations(A, B):
    target1, target2 = A[0], B[0]
    a = get_rots(A, B, target1)
    b = get_rots(A, B, target2)
    c = get_rots(B, A, target1)
    d = get_rots(B, A, target2)

    ans = min(a, b, c, d)
    if ans == float('inf'):
        return -1
    return ans


A = [2, 1, 2, 4, 2, 2]
B = [5, 2, 6, 2, 3, 2]
print(minDominoRotations(A, B))
