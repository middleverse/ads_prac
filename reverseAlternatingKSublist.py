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


def reverse_alternate_k_elements(head, k):
    if k <= 1 or head is None:
        return head

    previous, current, next = None, head, None
    skip = False
    while True:
        end_of_first_half = previous
        end_of_sublist = current
        counter = k
        while counter > 0 and current is not None:   
            if skip:
                previous = current
                current = current.next
            else: 
                next = current.next
                current.next = previous
                previous = current
                current = next
            counter -= 1

        if not skip:
            end_of_sublist.next = current
        
            if end_of_first_half is not None:
                end_of_first_half.next = previous    
            else:
                end_of_first_half = previous
                head = end_of_first_half
            previous = end_of_sublist
        
        if current is None: 
            break
        skip = True if skip == False else False

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
  result = reverse_alternate_k_elements(head, 2)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
