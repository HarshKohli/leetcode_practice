# Author: Harsh Kohli
# Date created: 9/19/2020

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    count = 0
    ptr = head

    while count <= n:
        if ptr is not None:
            ptr = ptr.next
            count = count + 1
        else:
            return head.next

    ptr2 = head
    while ptr is not None:
        ptr = ptr.next
        ptr2 = ptr2.next

    ptr2.next = ptr2.next.next
    return head



a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

removed = removeNthFromEnd(a, 2)

ptr = removed

while ptr is not None:
    print(ptr.val)
    ptr = ptr.next

a = ListNode(1)

removed = removeNthFromEnd(a, 1)

ptr = removed

while ptr is not None:
    print(ptr.val)
    ptr = ptr.next
