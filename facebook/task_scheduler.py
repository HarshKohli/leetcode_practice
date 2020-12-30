# Author: Harsh Kohli
# Date created: 11/28/2020

from queue import PriorityQueue


def leastInterval_slow(tasks, n):
    count_map = {}
    for task in tasks:
        if task in count_map:
            count_map[task] = count_map[task] - 1
        else:
            count_map[task] = - 1

    heap = PriorityQueue()
    for task, count in count_map.items():
        heap.put((count, task))

    banned_queue = []
    count = 0

    while not heap.empty():
        candidates = []
        next_task = None
        while not heap.empty():
            new_task = heap.get()
            if new_task[1] in banned_queue:
                candidates.append(new_task)
            else:
                next_task = new_task
                break
        for candidate in candidates:
            heap.put(candidate)

        if next_task is not None:
            val, name = next_task
            new_val = val + 1
            if new_val != 0:
                heap.put((new_val, name))
            banned_queue.append(name)
        else:
            banned_queue.append('idle')
        if len(banned_queue) > 0 and count >= n:
            banned_queue = banned_queue[1:]
        count = count + 1

    return count


def leastInterval(tasks, n):
    freq_map = {}
    max_freq = 0
    for task in tasks:
        if task in freq_map:
            freq_map[task] = freq_map[task] + 1
        else:
            freq_map[task] = 1
        if freq_map[task] > max_freq:
            max_freq = freq_map[task]

    num_max = 0
    for _, freq in freq_map.items():
        if freq == max_freq:
            num_max = num_max + 1

    idle = n * (max_freq - 1) - (len(tasks) - max_freq) + (num_max - 1)
    if idle < 0:
        idle = 0

    return idle + len(tasks)




tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(leastInterval(tasks, n))
