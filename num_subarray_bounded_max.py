# Author: Harsh Kohli
# Date created: 11/7/2020

def get_num_bounded(A, R):
    answer, present_count = 0, 0
    for num in A:
        if num <= R:
            present_count = present_count + 1
            answer = answer + present_count
        else:
            present_count = 0
    return answer

def numSubarrayBoundedMax(A, L, R):
    return get_num_bounded(A, R) - get_num_bounded(A, L - 1)


A = [4, 1, 1]
L = 2
R = 3
print(numSubarrayBoundedMax(A, L, R))
