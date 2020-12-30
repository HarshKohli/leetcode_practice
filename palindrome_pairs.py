# Author: Harsh Kohli
# Date created: 11/19/2020

def get_remaining(left, right, word, size):
    can_palin = True
    p1, p2 = left, right
    while p2 < size:
        if word[p2] == word[p1]:
            p2 = p2 + 1
            p1 = p1 - 1
        else:
            can_palin = False
            break
    if can_palin:
        return word[:p1 + 1][::-1]
    return None


def get_remaining_rev(left, right, word, size):
    can_palin = True
    p1, p2 = left, right
    while p1 >= 0 and p2 < size:
        if word[p1] == word[p2]:
            p2 = p2 + 1
            p1 = p1 - 1
        else:
            can_palin = False
            break
    if can_palin:
        return word[p2:][::-1]
    return None


def palindromePairs(words):
    remaining_to_index = {}
    remaining_to_index_rev = {}
    all_palins = []
    all_emptys = []

    for i, word in enumerate(words):
        size = len(word)
        if size == 0:
            all_emptys.append(i)
            continue
        mid = int(size / 2)
        for index in range(mid, size + 1):
            cands1 = get_remaining(index - 1, index, word, size)
            cands2 = get_remaining(index - 1, index + 1, word, size)
            if cands1 is not None:
                if cands1 not in remaining_to_index:
                    remaining_to_index[cands1] = set()
                remaining_to_index[cands1].add(i)

            if cands2 is not None:
                if cands2 not in remaining_to_index:
                    remaining_to_index[cands2] = set()
                remaining_to_index[cands2].add(i)

        for index in range(mid - 1, -1, -1):
            cands1 = get_remaining_rev(index - 1, index + 1, word, size)
            cands2 = get_remaining_rev(index, index + 1, word, size)
            if cands1 is not None:
                if cands1 not in remaining_to_index_rev:
                    remaining_to_index_rev[cands1] = set()
                remaining_to_index_rev[cands1].add(i)

            if cands2 is not None:
                if cands2 not in remaining_to_index_rev:
                    remaining_to_index_rev[cands2] = set()
                remaining_to_index_rev[cands2].add(i)

        if size % 2 == 0:
            is_palin = get_remaining(mid - 1, mid, word, size)
            if is_palin is not None:
                all_palins.append(i)
        else:
            is_palin = get_remaining(mid - 1, mid + 1, word, size)
            if is_palin is not None:
                all_palins.append(i)

    palin_pairs = []

    for index, word in enumerate(words):
        if word == "":
            continue
        if word in remaining_to_index:
            for cand in remaining_to_index[word]:
                if cand != index:
                    palin_pairs.append([cand, index])

        if word in remaining_to_index_rev:
            for cand in remaining_to_index_rev[word]:
                if cand != index:
                    palin_pairs.append([index, cand])

    for palin in all_palins:
        for empty in all_emptys:
            palin_pairs.append([palin, empty])
            palin_pairs.append([empty, palin])

    return palin_pairs


#words = ["bb","bababab","baab","abaabaa","aaba","","bbaa","aba","baa","b"]
#words = ["abcd", "dcba", "lls", "s", "sssll"]
#words = ["a", "abc", "aba", ""]
#words = ["a", ""]
words = ["abababb","ccaacab","ccbcbbb","","bbc","cca","abcbbba","bcccaac","bab","caacca"]
print(palindromePairs(words))

# [[5,4],[5,6],[5,8]]
#
# [[0,5],[0,9],[9,0],[5,0],[1,5],[5,1],[2,5],[8,2],[5,2],[4,3],[7,4],[4,8],[6,0],[7,5],[5,7],[8,9],[9,5],[5,9]]
