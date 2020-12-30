# Author: Harsh Kohli
# Date created: 9/11/2020

import heapq

def minMeetingRooms(intervals):
    rooms = 0
    for interval1 in intervals:
        count = 0
        for interval2 in intervals:
            if interval1[0] >= interval2[0] and interval1[0] < interval2[1]:
                count = count + 1
        if count > rooms:
            rooms = count
    return rooms


intervals = [[0, 30], [5, 10], [15, 20]]
num_rooms = minMeetingRooms(intervals)
print(num_rooms)
