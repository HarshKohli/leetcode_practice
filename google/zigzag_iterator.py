# Author: Harsh Kohli
# Date created: 1/18/2021

class ZigzagIterator:
    def __init__(self, v1, v2):
        size1, size2 = len(v1), len(v2)
        remaining = set()
        combined = []
        if size1 > 0:
            remaining.add(0)
            combined.append(v1)
        if size2 > 0:
            remaining.add(len(combined))
            combined.append(v2)
        self.zigzag = []
        ptr = 0
        while len(remaining) > 0:
            to_remove = []
            for index in remaining:
                self.zigzag.append(combined[index][ptr])
                if ptr == len(combined[index]) - 1:
                    to_remove.append(index)
            ptr = ptr + 1
            for x in to_remove:
                remaining.discard(x)
        self.ptr = 0

    def next(self) -> int:
        to_return = self.zigzag[self.ptr]
        self.ptr = self.ptr + 1
        return to_return

    def hasNext(self) -> bool:
        if self.ptr >= len(self.zigzag):
            return False
        return True
