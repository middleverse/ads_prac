# ===================== 
# Find Cycle Start Node
# =====================

# PROBLEM STATEMENT
# Given the head of a Singly LinkedList that contains a cycle, 
# write a function to find the starting node of the cycle.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# function returns start of cycle
def find_cycle_start(head):
    slow, fast = head, head
    cycle_start = None
    # move fast and slow pointers, up by 2 and 1 respectively
    # when they meet again, we can count the cycle length
    # then we find start of cycle knowing cycle length and find_start function
    while fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if (slow == fast):
            cycle_length = count_cycle_length(slow)
            # find cycle start
            cycle_start = find_start(head, cycle_length)
            break
    return cycle_start

# return start node
# create to pointers to head, first and second
# move second up by cycle_length
# then move both up by 1
# when they meet, we've found start node
def find_start(head, cycle_length):
    first, second = head, head
    while(cycle_length > 0):
        second = second.next
        cycle_length -= 1
    while (first != second):
        first = first.next
        second = second.next
    return first 

# return cycle length
def count_cycle_length(slow):
    current = slow
    length = 0
    while current.next != slow:
        current = current.next
        length += 1
    return length + 1

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

main()
