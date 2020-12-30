# Author: Harsh Kohli
# Date created: 11/29/2020

class LRUCache:
    class Node:
        def __init__(self, val, key, next=None, prev=None):
            self.val = val
            self.next = next
            self.prev = prev
            self.key = key

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head, self.tail = None, None
        self.count = 0
        self.key_node_dict = {}

    def get(self, key: int) -> int:
        if key not in self.key_node_dict:
            return -1
        node = self.key_node_dict[key]
        if node == self.head:
            return node.val
        if node.next is not None and node.prev is not None:
            node.next.prev = node.prev
            node.next.prev.next = node.next
        elif node.next is None:
            node.prev.next = None
            self.tail = node.prev
            node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_node_dict:
            node = self.key_node_dict[key]
            node.val = value
            if node == self.head:
                return
            if node.next is not None and node.prev is not None:
                node.next.prev = node.prev
                node.next.prev.next = node.next
            elif node.next is None:
                node.prev.next = None
                self.tail = node.prev
                node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            node = self.Node(value, key)
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                node.next = self.head
                self.head.prev = node
                self.head = node
            self.key_node_dict[key] = node
            self.count = self.count + 1
            if self.count > self.capacity:
                temp = self.tail
                self.tail = temp.prev
                self.tail.next = None
                self.count = self.capacity
                del self.key_node_dict[temp.key]

obj = LRUCache(2)

obj.put(2, 1)
obj.put(1, 1)
obj.put(2, 3)
obj.put(4, 1)
print(obj.get(1))
print(obj.get(2))

