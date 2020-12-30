# Author: Harsh Kohli
# Date created: 12/5/2020

from queue import PriorityQueue


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


def employeeFreeTime(schedule):
    employees = len(schedule)
    ptrs = [0 for _ in range(employees)]
    pq = PriorityQueue()
    for emp_no, one_sched in enumerate(schedule):
        window = one_sched[0]
        pq.put((window.start, emp_no, window))

    answers = []
    max_end = -1

    while not pq.empty():
        _, emp_no, window = pq.get()
        start, end = window.start, window.end
        if start > max_end and max_end != -1:
            ans_window = Interval(max_end, start)
            answers.append(ans_window)
        if max_end == -1 or end > max_end:
            max_end = end
        ptrs[emp_no] = ptrs[emp_no] + 1
        if ptrs[emp_no] < len(schedule[emp_no]):
            new_sched = schedule[emp_no][ptrs[emp_no]]
            pq.put((new_sched.start, emp_no, new_sched))

    return answers

