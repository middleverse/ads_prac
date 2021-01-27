from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse_sub_list(head, p, q):
    node = head
    first_half_tail = None
    while (p > 1):
        first_half_tail = node
        node = node.next
        p -= 1
        q -= 1
     
    # now node points to start
    sublist_end = node # start node will become end
    previous, current, next = None, node, None
    while q > 0:
        next = current.next
        current.next = previous
        previous = current
        current = next
        q -= 1

    # we've got a reversed sublist
    sublist_end.next = current # connect sublist and second half
    if first_half_tail is not None:
        first_half_tail.next = previous # connect first half and sublist
    else:
        head = previous
    return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 1, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
