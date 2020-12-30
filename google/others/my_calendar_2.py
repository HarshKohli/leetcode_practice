# Author: Harsh Kohli
# Date created: 10/19/2020


class MyCalendarTwo:

    def __init__(self):
        self.ranges = []

    def is_overlapping(self, range, all_ranges):
        x, y = range
        for a, b in all_ranges:
            if a <= x < b:
                return True
            if a < y <= b:
                return True
            if a <= x and b >= y:
                return True
            if x <= a and y >= b:
                return True
        return False

    def book(self, start: int, end: int) -> bool:
        # count = 0
        double_ranges = []
        for x, y in self.ranges:
            if start <= x < end:
                # count = count + 1
                double_range = (x, min(y, end))
                if self.is_overlapping(double_range, double_ranges):
                    return False
                double_ranges.append(double_range)
            elif start < y <= end:
                # count = count + 1
                double_range = (max(start, x), y)
                if self.is_overlapping(double_range, double_ranges):
                    return False
                double_ranges.append(double_range)
            elif start <= x and end >= y:
                double_range = (x, y)
                if self.is_overlapping(double_range, double_ranges):
                    return False
                double_ranges.append(double_range)
            elif x <= start and y >= end:
                double_range = (start, end)
                if self.is_overlapping(double_range, double_ranges):
                    return False
                double_ranges.append(double_range)

        self.ranges.append((start, end))
        return True


# calendar = MyCalendarTwo()
# x = calendar.book(10, 20)
# print(x)
# x = calendar.book(50, 60)
# print(x)
# x = calendar.book(10, 40)
# print(x)
# x = calendar.book(5, 15)
# print(x)
# x = calendar.book(5, 10)
# print(x)
# x = calendar.book(25, 55)
# print(x)


calendar = MyCalendarTwo()

ranges = [[],[12,26],[70,85],[55,67],[2,13],[3,18],[91,100],[13,26],[17,27],[41,55],[15,26],[50,68],[34,52],[95,100],[23,33],[89,100],[27,43],[80,95],[97,100],[28,47],[45,58],[76,93],[56,75],[91,100],[61,77],[36,49],[18,32],[96,100],[96,100],[67,86],[46,64],[95,100],[17,35],[8,27],[4,14],[30,43],[74,89],[77,95],[98,100],[31,41],[35,53]]

# for limits in ranges:
#     if len(limits) == 2:
#         start, end = limits[0], limits[1]
#         print(calendar.book(start, end))



for limits in ranges:
    if len(limits) == 2:
        start, end = limits[0], limits[1]
        print(calendar.book(start, end))
