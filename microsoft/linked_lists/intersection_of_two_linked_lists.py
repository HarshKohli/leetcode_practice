# Author: Harsh Kohli
# Date created: 11/19/2020

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(headA, headB):
        size1, size2 = 0, 0
        ptr1, ptr2 = headA, headB

        while ptr1 is not None:
            ptr1 = ptr1.next
            size1 = size1 + 1

        while ptr2 is not None:
            ptr2 = ptr2.next
            size2 = size2 + 1

        big, small = headA, headB
        if size2 > size1:
            big = headB
            small = headA
            temp = size1
            size1 = size2
            size2 = temp

        diff = size1 - size2
        ptr1, ptr2 = big, small

        count = 0
        while count != diff:
            ptr1 = ptr1.next
            count = count + 1

        while ptr1 is not None and ptr2 is not None:
            if ptr1 == ptr2:
                return ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return None
