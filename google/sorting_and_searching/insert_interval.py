# Author: Harsh Kohli
# Date created: 10/15/2020

def is_overlapping(interval1, interval2):
    if interval2[0] >= interval1[0] and interval2[0] <= interval1[1]:
        return True
    if interval2[1] >= interval1[0] and interval2[1] <= interval1[1]:
        return True
    if interval1[0] >= interval2[0] and interval1[0] <= interval2[1]:
        return True
    if interval1[1] >= interval2[0] and interval1[1] <= interval2[1]:
        return True
    return False


def merge(int1, int2):
    start = min(int1[0], int2[0])
    end = max(int1[1], int2[1])
    return [start, end]


def insert(intervals, newInterval):
    if len(intervals) == 0:
        return [newInterval]
    new_intervals = []
    found = False
    for num, interval in enumerate(intervals):
        if is_overlapping(interval, newInterval):
            new_interval = merge(interval, newInterval)
            new_intervals.append(new_interval)
            found = True
            break
        else:
            new_intervals.append(interval)
    if found:
        for index in range(num + 1, len(intervals)):
            interval = intervals[index]
            compare_with = new_intervals[-1]
            if is_overlapping(interval, compare_with):
                new_interval = merge(interval, compare_with)
                new_intervals.pop()
                new_intervals.append(new_interval)
            else:
                new_intervals.append(interval)
        return new_intervals
    else:
        inserted = []
        flag = False
        for interval in new_intervals:
            if interval[0] > newInterval[0] and not flag:
                inserted.append(newInterval)
                flag = True
            inserted.append(interval)
        if not flag:
            inserted.append(newInterval)
        return inserted


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
merged = insert(intervals, newInterval)
print(merged)
