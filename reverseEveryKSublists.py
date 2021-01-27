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

def reverse_every_k_elements(head, k):
    if k <= 1 or head is None: 
        return head

    # reverse the next 3
    previous, current = None, head
    while True:
        first_half_tail = previous 
        next = None
        sublist_end = current
        counter = k
        while counter > 0 and current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
            counter -= 1

        sublist_end.next = current
        if first_half_tail is not None:
            first_half_tail.next = previous
        else:
            first_half_tail = previous
            head = first_half_tail

        if current is None:
            break
        
        previous = sublist_end
    return head

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_every_k_elements(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()







