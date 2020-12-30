# Author: Harsh Kohli
# Date created: 11/19/2020

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    ptr = head
    prev = None
    while ptr != None:
        temp = ptr.next
        ptr.next = prev
        prev = ptr
        ptr = temp
    return prev


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

new_head = reverseList(a)
while new_head != None:
    print(new_head.val)
    new_head = new_head.next
