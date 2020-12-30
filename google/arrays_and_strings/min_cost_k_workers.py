# Author: Harsh Kohli
# Date created: 9/11/2020

from queue import PriorityQueue


def mincostToHireWorkers(quality, wage, K):
    ratios = [w / q for w, q in zip(wage, quality)]
    workers = [(r, q, w) for r, q, w in zip(ratios, quality, wage)]
    workers = sorted(workers)

    pQueue = PriorityQueue()
    min_quality_sum = 0.0
    cost = float('inf')

    for r, q, w in workers:
        pQueue.put(-q)
        min_quality_sum = min_quality_sum + q

        if pQueue.qsize() > K:
            max_quality = pQueue.get()
            min_quality_sum = min_quality_sum + max_quality

        if pQueue.qsize() == K:
            new_cost = r * min_quality_sum
            if new_cost < cost:
                cost = new_cost

    return cost


quality = [3, 1, 10, 10, 1]
wage = [4, 8, 2, 2, 7]
K = 3
min_cost = mincostToHireWorkers(quality, wage, K)
print(min_cost)
