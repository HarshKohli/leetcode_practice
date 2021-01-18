# Author: Harsh Kohli
# Date created: 1/18/2021

class ValidWordAbbr:

    def __init__(self, dictionary):
        self.words = {}
        for word in dictionary:
            num = len(word) - 2
            if num > 0:
                to_add = word[0] + str(num) + word[len(word) - 1]
            elif num == 0:
                to_add = word[0] + word[len(word) - 1]
            else:
                to_add = word[0]
            if to_add not in self.words:
                self.words[to_add] = set()
            self.words[to_add].add(word)

    def isUnique(self, word: str) -> bool:
        num = len(word) - 2
        if num > 0:
            to_add = word[0] + str(num) + word[len(word) - 1]
        elif num == 0:
            to_add = word[0] + word[len(word) - 1]
        else:
            to_add = word[0]
        if to_add not in self.words:
            return True
        if to_add in self.words:
            if word in self.words[to_add] and len(self.words[to_add]) == 1:
                return True
        return False
