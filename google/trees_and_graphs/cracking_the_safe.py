# Author: Harsh Kohli
# Date created: 10/3/2020

from copy import deepcopy


def crackSafe(n, k):
    num_combs = k ** n
    init = [('', set())]
    while True:
        combs = []
        for num in range(k):
            for x, matched in init:
                comb = x + str(num)
                new_matched = deepcopy(matched)
                if len(comb) >= n:
                    to_match = comb[len(comb) - n:]
                    new_matched.add(to_match)
                    if len(new_matched) == num_combs:
                        return comb
                combs.append((comb, new_matched))
        init = combs


n = 1
k = 8
print(crackSafe(n, k))
