# Author: Harsh Kohli
# Date created: 11/5/2020

def get_overlap(s1, e1, s2, e2):
    start = max(s1, s2)
    end = min(e1, e2)
    if end >= start:
        return [start, end]
    return None


def intervalIntersection(A, B):
    ptr = 0
    intervals = []
    for interval in A:
        start, end = interval[0], interval[1]
        end2 = None
        while ptr < len(B):
            start2, end2 = B[ptr]
            if start2 > end:
                break
            overlap = get_overlap(start, end, start2, end2)
            if overlap is not None:
                intervals.append(overlap)
            ptr = ptr + 1
        if end2 is not None and end2 > end and ptr > 0:
            ptr = ptr - 1
    return intervals


A = [[0,5],[12,14],[15,18]]
B = [[11,15],[18,19]]
print(intervalIntersection(A, B))
