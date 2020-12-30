# Author: Harsh Kohli
# Date created: 10/28/2020

def recurse(s, wordDict, index, markers):
    if index == len(s):
        return True
    if index > len(s):
        return False
    if index in markers:
        return markers[index]
    for word in wordDict:
        size = len(word)
        if index + size > len(s):
            continue
        if s[index: index + size] == word:
            does_match = recurse(s, wordDict, index + size, markers)
            if does_match:
                markers[index] = True
                return True
    markers[index] = False
    return False


def wordBreak(s, wordDict):
    return recurse(s, wordDict, 0, {})


s = "applepenapple"
wordDict = ["apple", "pen"]
print(wordBreak(s, wordDict))
