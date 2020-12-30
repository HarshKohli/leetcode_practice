# Author: Harsh Kohli
# Date created: 9/19/2020

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    sum_list, sum_ptr = None, None
    ptr1, ptr2, carry = l1, l2, 0
    while True:
        minisum = 0
        if ptr1 != None:
            minisum = minisum + ptr1.val
            ptr1 = ptr1.next
        if ptr2 != None:
            minisum = minisum + ptr2.val
            ptr2 = ptr2.next
        minisum = minisum + carry
        carry = int(minisum / 10)
        new_val = minisum % 10
        new_node = ListNode(new_val)
        if sum_list == None:
            sum_list = new_node
            sum_ptr = new_node
        else:
            sum_ptr.next = new_node
            sum_ptr = new_node
        if ptr1 == None and ptr2 == None:
            break
    if carry != 0:
        new_node = ListNode(carry)
        sum_ptr.next = new_node
    return sum_list


a = ListNode(2)
b = ListNode(4)
c = ListNode(3)

a.next = b
b.next = c

c = ListNode(5)
d = ListNode(6)
e = ListNode(4)

c.next = d
d.next = e

sum = addTwoNumbers(a, c)

ptr = sum

while ptr is not None:
    print(ptr.val)
    ptr = ptr.next

x = ListNode(5)
y = ListNode(5)

sum = addTwoNumbers(x, y)

ptr = sum

while ptr is not None:
    print(ptr.val)
    ptr = ptr.next
