# ============================
# Rearrange LinkedList Problem
# ============================

# PROBLEM STATEMENT
# Given the head of a Singly LinkedList, write a method to modify the 
# LinkedList such that the nodes from the second half of the LinkedList 
# are inserted alternately to the nodes from the first half in reverse 
# order. 

# EXAMPLE
# So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, 
# your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

# NOTE: Assume linkedList is always even

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()

def reorder(head):
    slow, fast = head, head
    
    # get to the middle element
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    # reverse list starting from slow
    second_half = reverse_list(slow)
    first_half = head

    # iterate through first half, adding elements from second_half one by one
    # second_half is reversed hence elements will be in the correct order when added
    while second_half.next is not None:
        first_half_next = first_half.next
        second_half_next = second_half.next
        first_half.next = second_half
        second_half.next = first_half_next
        second_half = second_half_next
        first_half = first_half_next
        

def reverse_list(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()


main()
