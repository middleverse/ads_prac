from __future__ import print_function
from heapq import *


class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

    # used for the min-heap
    def __lt__(self, other):
        return self.val < other.val

def merge_lists(lists):
    result_head, result_tail = None, None
    min_heap = []

    for root in lists:
        if root is not None:
            heappush(min_heap, root)
    
    while min_heap:
        smallest_node = heappop(min_heap)
        if result_head is None:
            result_head = result_tail = smallest_node
        else:
            result_tail.next = smallest_node
            result_tail = result_tail.next

        if smallest_node.next is not None:
            heappush(min_heap, smallest_node.next)

    return result_head


def main():
  l1 = ListNode(2)
  l1.next = ListNode(6)
  l1.next.next = ListNode(8)

  l2 = ListNode(3)
  l2.next = ListNode(6)
  l2.next.next = ListNode(7)

  l3 = ListNode(1)
  l3.next = ListNode(3)
  l3.next.next = ListNode(4)

  result = merge_lists([l1, l2, l3])
  print("Here are the elements form the merged list: ", end='')
  while result != None:
    print(str(result.val) + " ", end='')
    result = result.next


main()

