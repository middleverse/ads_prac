# =========================
# Remove Duplicates Problem
# =========================

# PROBLEM STATEMENT
# Given an array of sorted numbers, remove all duplicates from it. 
# You should not use any extra space; after removing the duplicates 
# in-place return the length of the subarray that has no duplicate in it.

# EXAMPLE
# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

def remove_duplicates(arr):
    left, duplicates = 0, 0

    # iterate over all array items
    # if right is equal to left, we've found a duplicate
    # if right is not equal to left, shift left to the same index as right
    for right in range(1, len(arr)):
            if arr[right] == arr[left]:
                duplicates += 1
            else:
                left = right
    # return array length with duplicates
    return len(arr) - duplicates

def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()


