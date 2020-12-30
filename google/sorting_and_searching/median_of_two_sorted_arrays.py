# Author: Harsh Kohli
# Date created: 10/12/2020

def findMedianSortedArrays(nums1, nums2):
    if len(nums2) > len(nums1):
        m, n = len(nums2), len(nums1)
        a, b = nums2, nums1
    else:
        m, n = len(nums1), len(nums2)
        a, b = nums1, nums2
    is_even = False
    if (m + n) % 2 == 0:
        is_even = True
    if m > 0 and n > 0:
        if a[m - 1] <= b[0]:
            x = a[int((m + n - 1) / 2)]
            if is_even:
                second = int((m + n - 1) / 2) + 1
                if second >= m:
                    y = b[0]
                else:
                    y = a[second]
                return float((x + y) / 2)
            else:
                return float(x)
        if b[n - 1] <= a[0]:
            mid_pos = int((m + n - 1) / 2)
            if mid_pos >= n:
                mid_pos = mid_pos - n
                x = a[mid_pos]
                if is_even:
                    y = a[mid_pos + 1]
                    return float((x + y) / 2)
                else:
                    return float(x)
            else:
                x = b[mid_pos]
                mid_pos = mid_pos - n
                if is_even:
                    y = a[mid_pos + 1]
                    return float((x + y) / 2)
                else:
                    return float(x)

        size = int((m + n + 1) / 2)
        left, right = size - n + 1, size
        found = False
        while True:
            mid = int((left + right) / 2)
            last_a = mid - 1
            last_b = (size - mid) - 1
            if last_b >= 0 and last_b < (n - 1) and last_a < (m - 1) and a[last_a] <= b[last_b + 1] and b[last_b] <= a[last_a + 1]:
                max_left = max(a[last_a], b[last_b])
                if is_even:
                    max_right = min(a[last_a + 1], b[last_b + 1])
                    median = (max_left + max_right) / 2
                else:
                    median = max_left
                found = True
                break
            if last_b == n - 1:
                max_right = max(a[last_a], b[last_b])
                if is_even:
                    max_left = a[last_a + 1]
                    median = (max_left + max_right) / 2
                else:
                    median = max_right
                found = True
                break
            if last_b < (n - 1) and a[last_a] > b[last_b + 1]:
                right = mid - 1
            else:
                if last_b == -1:
                    x = a[last_a]
                    if is_even:
                        y = min(a[last_a + 1], b[0])
                        median = (x + y) / 2
                    else:
                        median = x
                    found = True
                    break
                left = mid + 1
        if found:
            return float(median)
        else:
            x = a[left - 1]
            if is_even:
                if m > left and n > (size - left) - 1:
                    y = min(a[left], b[(size - left) - 1])
                    return (x + y) / 2
                else:
                    y = a[left]
                    return (x + y) / 2
            else:
                return max((x, b[size - left - 1]))
    else:
        if m == 1:
            return float(a[0])
        if is_even:
            x = a[int((m / 2) - 1)]
            y = a[int(m / 2)]
            return float((x + y) / 2)
        else:
            return float(a[int((m / 2))])


# nums1 = [4, 20, 32, 50, 55, 61]
# nums2 = [1, 15, 22, 30, 70]
nums1 = [3]
nums2 = [1, 2, 4]
median = findMedianSortedArrays(nums1, nums2)
print(median)
