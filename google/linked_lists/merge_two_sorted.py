# Author: Harsh Kohli
# Date created: 9/19/2020

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    ptr1, ptr2 = l1, l2
    combined, combined_ptr = None, None
    while True:
        to_add = None
        if ptr1 is not None and ptr2 is not None:
            if ptr1.val < ptr2.val:
                to_add = ptr1.val
                ptr1 = ptr1.next
            else:
                to_add = ptr2.val
                ptr2 = ptr2.next
        else:
            if ptr1 is not None:
                to_add = ptr1.val
                ptr1 = ptr1.next
            elif ptr2 is not None:
                to_add = ptr2.val
                ptr2 = ptr2.next
            else:
                break
        if to_add is not None:
            new_node = ListNode(to_add)
            if combined is None:
                combined = new_node
                combined_ptr = new_node
            else:
                combined_ptr.next = new_node
                combined_ptr = new_node
    return combined


a = ListNode(1)
b = ListNode(2)
c = ListNode(4)

a.next = b
b.next = c

d = ListNode(1)
e = ListNode(3)
f = ListNode(4)

d.next = e
e.next = f

sorted_list = mergeTwoLists(a, d)

ptr = sorted_list

while ptr is not None:
    print(ptr.val)
    ptr = ptr.next
