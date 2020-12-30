# Author: Harsh Kohli
# Date created: 10/22/2020

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def retreive_last(root):
    node = root
    while node.next.next is not None:
        node = node.next
    last = node.next
    node.next = None
    return last

def reorderList(head):
    if head is None:
        return
    size = 0
    node = head
    nodes = []
    while node != None:
        size = size + 1
        nodes.append(node)
        node = node.next
    hops = int(size/2)
    root = head
    for hop in range(hops):
        last = nodes[size - 1 - hop]
        nodes[size - 2 - hop].next = None
        #last = retreive_last(root)
        last.next = root.next
        root.next = last
        root = root.next.next


