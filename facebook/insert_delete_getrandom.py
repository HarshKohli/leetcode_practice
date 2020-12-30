# Author: Harsh Kohli
# Date created: 11/30/2020

import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.full_map = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.full_map:
            return False
        self.full_map[val] = 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.full_map:
            del self.full_map[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(list(self.full_map.keys()))
