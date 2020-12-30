# Author: Harsh Kohli
# Date created: 11/5/2020

def isSorted(word1, word2, order_map):
    one_len, two_len = len(word1), len(word2)
    size = min(one_len, two_len)
    for a, b in zip(word1[:size], word2[:size]):
        if a != b:
            num1, num2 = order_map[a], order_map[b]
            if num1 < num2:
                return True
            else:
                return False
    if one_len > two_len:
        return False
    return True


def isAlienSorted(words, order):
    order_map = {}
    num = 0
    for x in order:
        order_map[x] = num
        num = num + 1
    for index in range(len(words) - 1):
        word1, word2 = words[index], words[index + 1]
        if not isSorted(word1, word2, order_map):
            return False
    return True


words = ["leetcode", "hello"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(isAlienSorted(words, order))
