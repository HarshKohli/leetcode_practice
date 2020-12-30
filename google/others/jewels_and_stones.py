# Author: Harsh Kohli
# Date created: 10/19/2020

def numJewelsInStones(J, S):
    count = 0
    for s in S:
        if s in J:
            count = count + 1
    return count

J = "aA"
S = "aAAbbbb"
print(numJewelsInStones(J, S))
