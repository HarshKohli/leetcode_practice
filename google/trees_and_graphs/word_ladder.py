# Author: Harsh Kohli
# Date created: 9/28/2020

from queue import Queue


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    nodes = []
    first_node = Node(beginWord)
    adj_map = {}
    nodes.append(first_node)

    adjacents = []
    for index in range(1, len(beginWord) - 1):
        adjacent = beginWord[:index] + '.' + beginWord[index + 1:]
        adjacents.append(adjacent)
    first, last = '.' + beginWord[1:], beginWord[:len(beginWord) - 1] + '.'
    adjacents.append(first)
    adjacents.append(last)
    for adj in adjacents:
        adj_map[adj] = [first_node]

    for word in wordList:
        new_node = Node(word)

        adjacents = []
        for index in range(1, len(word) - 1):
            adjacent = word[:index] + '.' + word[index + 1:]
            adjacents.append(adjacent)
        first, last = '.' + word[1:], word[:len(word) - 1] + '.'
        adjacents.append(first)
        adjacents.append(last)

        for adj in adjacents:
            if adj not in adj_map:
                adj_map[adj] = [new_node]
            else:
                for node in adj_map[adj]:
                    if node.next is None:
                        node.next = [new_node]
                    else:
                        node.next.append(new_node)
                    if new_node.next is None:
                        new_node.next = [node]
                    else:
                        new_node.next.append(node)
                adj_map[adj].append(new_node)
        # for node in nodes:
        #     count = 0
        #     for a, b in zip(node.val, word):
        #         if a != b:
        #             count = count + 1
        #     if count == 1:
        #         if node.next is None:
        #             node.next = [new_node]
        #         else:
        #             node.next.append(new_node)
        #         if new_node.next is None:
        #             new_node.next = [node]
        #         else:
        #             new_node.next.append(node)
        nodes.append(new_node)
    q = Queue()
    q.put(first_node)
    q.put(None)
    seen = set()
    ladder = 1
    found = False
    while not q.empty():
        node = q.get()
        if node in seen:
            continue
        if node is None:
            ladder = ladder + 1
            if q.empty():
                break
            q.put(None)
            continue
        if node.val == endWord:
            found = True
            break
        if node.next is not None:
            for child in node.next:
                if child.val not in seen:
                    q.put(child)
        seen.add(node)

    if found:
        return ladder
    else:
        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
ll = ladderLength(beginWord, endWord, wordList)
print(ll)
