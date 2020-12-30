# Author: Harsh Kohli
# Date created: 9/19/2020


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):
    new_head, new_ptr = None, None
    ptr = head
    node_index_map, new_index_node_map = {}, {}
    pos = 0
    while ptr is not None:
        node_index_map[ptr] = pos
        new_val = ptr.val
        new_node = Node(new_val)
        new_index_node_map[pos] = new_node
        if new_head is None:
            new_head = new_node
            new_ptr = new_node
        else:
            new_ptr.next = new_node
            new_ptr = new_node
        pos = pos + 1
        ptr = ptr.next

    ptr = head
    random_indices = []
    while ptr is not None:
        random_ptr = ptr.random
        if random_ptr is None:
            random_indices.append(None)
        else:
            random_indices.append(node_index_map[random_ptr])
        ptr = ptr.next

    ptr = new_head
    count = 0
    while ptr is not None:
        new_random = random_indices[count]
        if new_random is not None:
            rand_ptr = new_index_node_map[new_random]
            ptr.random = rand_ptr
        count = count + 1
        ptr = ptr.next

    return new_head
