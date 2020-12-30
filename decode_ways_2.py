# Author: Harsh Kohli
# Date created: 11/7/2020

def recurse(s, index, permutation_map, size):
    if index == size:
        return 1
    num = s[index]
    if num == '0':
        return 0
    if index in permutation_map:
        return permutation_map[index]
    single_perms = recurse(s, index + 1, permutation_map, size)
    if num == '*':
        single_perms = single_perms * 9
    double_perms = 0
    if index != size - 1:
        double_num = s[index: index + 2]
        if double_num == '**':
            double_perms = recurse(s, index + 2, permutation_map, size)
            double_perms = double_perms * 15
        elif double_num[0] == '*':
            double_perms = recurse(s, index + 2, permutation_map, size)
            if 0 <= int(double_num[1]) <= 6:
                double_perms = double_perms * 2
        elif double_num[1] == '*':
            if double_num[0] == '1':
                double_perms = recurse(s, index + 2, permutation_map, size)
                double_perms = double_perms * 9
            elif double_num[0] == '2':
                double_perms = recurse(s, index + 2, permutation_map, size)
                double_perms = double_perms * 6
        else:
            if 1 <= int(double_num) <= 26:
                double_perms = recurse(s, index + 2, permutation_map, size)

    total_perms = single_perms + double_perms
    total_perms = total_perms % (10**9 + 7)
    permutation_map[index] = total_perms
    return total_perms


def numDecodings(s):
    return recurse(s, 0, {}, len(s))


s = "**"
print(numDecodings(s))
