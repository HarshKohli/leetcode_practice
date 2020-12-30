# Author: Harsh Kohli
# Date created: 10/28/2020

def recurse(index, s, ways_map):
    if index == len(s):
        return 1
    if s[:index + 1] in ways_map:
        return ways_map[s[:index + 1]]
    if int(s[index]) != 0:
        single_ways = recurse(index + 1, s, ways_map)
    else:
        return 0
    double_ways = 0
    if index != len(s) - 1 and 0 < int(s[index: index + 2]) < 27:
        double_ways = recurse(index + 2, s, ways_map)
    permutations = single_ways + double_ways
    ways_map[s[:index + 1]] = permutations
    return permutations


def numDecodings(s):
    ways_map = {}
    return recurse(0, s, ways_map)


s = "222010"
print(numDecodings(s))
