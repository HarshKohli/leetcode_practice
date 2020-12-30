# Author: Harsh Kohli
# Date created: 11/19/2020


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def recurse(node1, node2):
    if node1 is None and node2 is None:
        return None, 0
    next_node, carry = recurse(node1.next, node2.next)
    sum = node1.val + node2.val + carry
    new_val, new_carry = sum % 10, int(sum / 10)
    new_node = ListNode(new_val)
    new_node.next = next_node
    return new_node, new_carry


def recurse_single(node1, answer, diff, old_carry):
    if diff == 0:
        return answer, old_carry
    next_node, carry = recurse_single(node1.next, answer, diff - 1, old_carry)
    sum = node1.val + carry
    new_val, new_carry = sum % 10, int(sum / 10)
    new_node = ListNode(new_val)
    new_node.next = next_node
    return new_node, new_carry


def addTwoNumbers(l1, l2):
    size1, size2 = 0, 0
    ptr1, ptr2 = l1, l2

    while ptr1 is not None:
        ptr1 = ptr1.next
        size1 = size1 + 1

    while ptr2 is not None:
        ptr2 = ptr2.next
        size2 = size2 + 1

    big, small = l1, l2
    if size2 > size1:
        big = l2
        small = l1
        temp = size1
        size1 = size2
        size2 = temp

    diff = size1 - size2
    ptr1, ptr2 = big, small

    count = 0
    while count != diff:
        ptr1 = ptr1.next
        count = count + 1

    sum_head, carry = recurse(ptr1, ptr2)
    new_sum_head, carry = recurse_single(big, sum_head, diff, carry)

    if carry != 0:
        answer = ListNode(carry)
        answer.next = new_sum_head
        return answer

    return new_sum_head


a = ListNode(9)
b = ListNode(9)
c = ListNode(9)
h = ListNode(9)
j = ListNode(9)

a.next = b
b.next = c
c.next = h
h.next = j

d = ListNode(9)
e = ListNode(9)
f = ListNode(9)

d.next = e
e.next = f

answer = addTwoNumbers(a, d)
while answer != None:
    print(answer.val)
    answer = answer.next
