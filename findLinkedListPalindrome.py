# ==========================
# Find LinkedList Palindrome
# ==========================

# PROBLEM STATEMENT
# Given the head of a Singly LinkedList, write a method to check 
# if the LinkedList is a palindrome or not.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_palindromic_linked_list(head):
    if head is None or head.next is None:
        return True # empty or 1 length of list
    
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    # at this point we're in the middle with slow
    # reverse the second half of the list and then compare
    head_second_half = reverse_list(slow)
    head_second_half_copy = head_second_half
    # compare starting head and head_second_half until we reach end of both sides
    while head is not None and head_second_half is not None:
        if head.value != head_second_half.value:
            break # we don't return false here since we need to return list in original form
        head = head.next
        head_second_half = head_second_half.next
    # return list to normal
    reverse_list(head_second_half_copy)
    # check to see if both heads are at None, that means its a palindrome
    if head is None or head_second_half is None:
        return True
    # while loop stopped before reaching None from both sides, not a palindrome
    return False

# reverse a list starting from head
def reverse_list(head):
    prev = None
    while (head is not None):
        next = head.next # next is placeholder for next head
        head.next = prev # main reversal step
        prev = head 
        head = next
    return prev

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

main()







