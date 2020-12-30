# Author: Harsh Kohli
# Date created: 11/19/2020

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    fast, slow = head, head
    while True:
        if fast is None or fast.next is None or fast.next.next is None:
            return False
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
