# ==================
# Target Sum Problem
# ==================

# PROBLEM STATEMENT
# Given an array of sorted numbers and a target sum, 
# find a pair in the array whose sum is equal to the given target.

def pair_with_targetsum(arr, target_sum):
    left, right = 0, len(arr) - 1

    while left != right:
        cur_sum = arr[left] + arr[right]
        if target_sum > cur_sum:
            left += 1
        elif target_sum < cur_sum:
            right -= 1
        else:
            return [left, right]    
      
    return [-1, -1]
    
def main():
  print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum([2, 5, 9, 11], 11))


main()