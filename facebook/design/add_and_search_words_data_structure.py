# Author: Harsh Kohli
# Date created: 11/30/2020

class WordDictionary:
    class Node:
        def __init__(self):
            self.is_word = False
            self.children = [None for _ in range(26)]

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()

    def add_recurse(self, root, word, index):
        x = word[index]
        ptr = ord(x) - 97
        if root.children[ptr] is None:
            next_node = self.Node()
            root.children[ptr] = next_node
        else:
            next_node = root.children[ptr]
        if index == len(word) - 1:
            next_node.is_word = True
        else:
            self.add_recurse(next_node, word, index + 1)

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.add_recurse(self.root, word, 0)

    def search_recurse(self, root, word, index):
        if root is None:
            return False
        if index == len(word):
            if root.is_word:
                return True
            else:
                return False
        x = word[index]
        if x != '.':
            ptr = ord(x) - 97
            if root.children[ptr] is None:
                return False
            return self.search_recurse(root.children[ptr], word, index + 1)

        for child in root.children:
            found = self.search_recurse(child, word, index + 1)
            if found:
                return True

        return False

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.search_recurse(self.root, word, 0)
