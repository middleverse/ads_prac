# =======================
# Cycle In Circular Array 
# =======================

# PROBLEM STATEMENT
# We are given an array containing positive and negative numbers. Suppose the array contains 
# a number ‘M’ at a particular index. Now, if ‘M’ is positive we will move forward ‘M’ indices 
# and if ‘M’ is negative move backwards ‘M’ indices. You should assume that the array is circular 
# which means two things:
# If, while moving forward, we reach the end of the array, we will jump to the first element to 
# continue the movement.
# If, while moving backward, we reach the beginning of the array, we will jump to the last element 
# to continue the movement.
# Write a method to determine if the array has a cycle. The cycle should have more than one 
# element and should follow one direction which means the cycle should not contain both forward 
# and backward movements.

# EXAMPLE:
# Input: [1, 2, -1, 2, 2]
# Output: true
# Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0
# Input: [2, 1, -1, -2]
# Output: false
# Explanation: The array does not have any cycle.

def circular_array_loop_exists(arr):
    slow, fast = 0, 0

    for i in range(len(arr)):
        slow = i
        fast = i
        # while we're only going in one direction, keep checking
        count = 0 # make sure its not cyclic with one element (part of problem statment)
        while (arr[slow] >= 0 and arr[fast] >= 0) or (arr[slow] < 0 and arr[fast] < 0):
            fast += arr[fast]
            fast = fast % len(arr) # wrap around index on both sides
            if fast == slow and count > 0:
                return True
            count += 1
    return False


def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))


main()
