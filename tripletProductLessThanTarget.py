
# PROBLEM STATEMENT
# Given an array with positive numbers and a target number, find all of 
# its contiguous subarrays whose product is less than the target number.
from collections import deque

def find_subarrays(arr, target):
    result = []
    product = 1
    left = 0

    # iterate over all elements in arr
    for right in range(len(arr)):
        product *= arr[right]
        
        # if product is greater/less than target
        while product >= target and left < len(arr):
            product /= arr[left]
            left += 1
        
        temp_list = deque()
        for i in range(right, left-1, -1): # step bakcwards from right to left
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))
    return result

def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print()
  print(find_subarrays([8, 2, 6, 5], 50))

main()