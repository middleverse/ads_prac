# ===================
# Minimum Window Sort
# ===================

# PROBLEM STATEMENT
# Given an array, find the length of the smallest subarray in it 
# which when sorted will sort the whole array.

# EXAMPLE
# Input: [1, 2, 5, 3, 7, 10, 9, 12]
# Output: 5
# Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] 
# to make the whole array sorted
# NOTE: return 0 if already sorted

import math

def shortest_window_sort(arr):
    low, high = 0, len(arr) - 1
    # start from 0th element and shift towards right, stop at the first unsorted element
    while low < len(arr) - 1 and arr[low] <= arr[low + 1]:
        low += 1
    # array is sorted
    if low == len(arr) - 1:
        return 0 
    # start from the last element and shift left, stop at the first unsorted element
    while high > 0 and arr[high] >= arr[high - 1]:
        high -= 1
    # both low and high are now the first unsorted numbers on the low and high end
    # find the min and max elements in the subarray that starts from low and ends at high
    subarray_min = math.inf
    subarray_max = -math.inf
    for i in range(low, high + 1):
        subarray_min = min(subarray_min, arr[i])
        subarray_max = max(subarray_max, arr[i])
    # find the right place for the smallest element in subarray towards the left
    # at first element that is less than smallest element, stop shifting left
    while low > 0 and arr[low - 1] > subarray_min:
        low -= 1
    # do the same for right, except shift right and stop shifting when
    # first element that is larger than max element in subarray is encountered
    while high < len(arr) - 1 and arr[high + 1] < subarray_max:
        high += 1

    return high - low + 1

def main():
  print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
  print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
  print(shortest_window_sort([1, 2, 3]))
  print(shortest_window_sort([3, 2, 1]))


main()