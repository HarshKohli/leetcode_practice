# Author: Harsh Kohli
# Date created: 12/3/2020

def customSortString(S, T):
    occurence_dict = {}
    for x in S:
        occurence_dict[x] = 0

    answer = ''
    for x in T:
        if x in occurence_dict:
            occurence_dict[x] = occurence_dict[x] + 1
        else:
            answer = answer + x

    for x in S:
        for _ in range(occurence_dict[x]):
            answer = answer + x

    return answer


S = "cba"
T = "abcd"
print(customSortString(S, T))
