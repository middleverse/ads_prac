# ===========================
# Smaller Triplet Sum Problem
# ===========================


# PROBLEM STATEMENT
# Given an array arr of unsorted numbers and a target sum, count all triplets 
# in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three 
# different indices. Write a function to return the count of such triplets.

# EXAMPLE
# Input: [-1, 0, 2, 3], target=3 
# Output: 2
# Explanation: There are two triplets whose sum is less than the target: 
# [-1, 0, 3], [-1, 0, 2]

def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr) - 2):
        count += search_duplet(arr, target - arr[i], i)
    return count


def search_duplet(arr, target, first_elem):
    count = 0
    left, right = first_elem + 1, len(arr) - 1
    
    # use left and right pointers to check all elements for target pair
    while left < right:
        # found a triplet sum less than target
        if arr[left] + arr[right] < target:
            count += right - left
            left += 1
        # triplet sum is greater than target    
        else:
            right -= 1
    return count

def main():
  print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
  print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))

main()
