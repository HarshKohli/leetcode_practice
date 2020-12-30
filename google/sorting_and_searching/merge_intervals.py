# Author: Harsh Kohli
# Date created: 10/14/2020

def merge(intervals):
    if len(intervals) == 0:
        return []
    sorted_intervals = sorted(intervals)
    prev_max = None
    clustered = []
    for interval in sorted_intervals:
        if prev_max is None:
            clustered.append([interval])
            prev_max = interval[1]
        else:
            if interval[0] <= prev_max:
                clustered[-1].append(interval)
                if interval[1] > prev_max:
                    prev_max = interval[1]
            else:
                clustered.append([interval])
                prev_max = interval[1]

    ranges = []
    for cluster in clustered:
        upper = float('-inf')
        for interval in cluster:
            if interval[1] > upper:
                upper = interval[1]
        ranges.append([cluster[0][0], upper])

    return ranges

intervals = [[1,3],[2,6],[8,10],[15,18]]
ranges = merge(intervals)
print(ranges)
