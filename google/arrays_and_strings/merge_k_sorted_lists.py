# Author: Harsh Kohli
# Date created: 8/16/2020

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    ptrs = [0] * len(lists)
    outlist = []
    while True:
        list_num, min = 0, float('inf')
        for index, (ptr, list) in enumerate(zip(ptrs, lists)):
            if ptr < len(list):
                num = list[ptr]
                if num < min:
                    min = num
                    list_num = index
        if min == float('inf'):
            break
        else:
            outlist.append(lists[list_num][ptrs[list_num]])
            ptrs[list_num] = ptrs[list_num] + 1
    return outlist

def sift_down(arr, index):
    while True:
        left, right = 2 * index + 1, 2 * index + 2
        if left < len(arr) and arr[index].val > arr[left].val:
            temp = arr[index]
            arr[index] = arr[left]
            arr[left] = temp
        elif right < len(arr) and arr[index].val > arr[right].val:
            temp = arr[index]
            arr[index] = arr[right]
            arr[right] = temp
        else:
            break

def build_heap(arr):
    n = len(arr)
    mid = n // 2
    for index in range(mid, -1, -1):
        sift_down(arr, index)

def mergeKLists_lc(lists):
    ptrs = lists
    first, latest = None, None
    while True:
        list_num, min = 0, float('inf')
        for index, (ptr, list) in enumerate(zip(ptrs, lists)):
            if ptr != None:
                num = ptr.val
                if num < min:
                    min = num
                    list_num = index
        if min == float('inf'):
            break
        else:
            new_node = ListNode(val=min, next=None)
            if first == None:
                first = new_node
                latest = new_node
            else:
                latest.next = new_node
                latest = new_node
            ptrs[list_num] = ptrs[list_num].next
    return first

def mergeKLists_lc_2(lists):
    for node in lists:
        if node == []:
            return None
    heap = lists
    build_heap(heap)
    first, latest = None, None
    while len(heap) > 0:
        node = heap[0]
        if node == None or node == []:
            break
        new_node = ListNode(val=node.val, next=None)
        if first == None:
            first = new_node
        else:
            latest.next = new_node
        latest = new_node
        next_node = node.next
        if next_node != None:
            heap[0] = next_node
            sift_down(heap, 0)
        else:
            heap.pop(0)
            sift_down(heap, 0)
    return first


# lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
# sorted_list = mergeKLists(lists)
# print(sorted_list)

a = ListNode(val=1, next=None)
b = ListNode(val=4, next=None)
c = ListNode(val=5, next=None)

d = ListNode(val=1, next=None)
e = ListNode(val=3, next=None)
f = ListNode(val=4, next=None)

g = ListNode(val=2, next=None)
h = ListNode(val=6, next=None)

a.next = b
b.next = c

d.next = e
e.next = f

g.next = h
lists = [a, d, g]
#sorted_list = mergeKLists_lc_2(lists)

sorted_list = mergeKLists_lc_2([[],[]])

print('Done sorting')
