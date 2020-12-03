# ===========
# Cyclic Sort
# ===========

# PROBLEM STATEMENT
# Write a function to sort the objects in-place on their creation 
# sequence number in O(n) and without any extra space. For simplicity, 
# let’s assume we are passed an integer array containing only the 
# sequence numbers, though each number is actually an object.

def cyclic_sort(nums):
    i = 0
    # in place sorrt of a sequence
    while i < len(nums):
        correctIndex = nums[i] - 1
        # element at index i shouldn't belong there
        # swap it to its correct index
        if nums[i] != i + 1:
            nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
        else:
            i += 1
    return nums

def main():
  print(cyclic_sort([3, 1, 5, 4, 2]))
  print(cyclic_sort([2, 6, 4, 3, 1, 5]))
  print(cyclic_sort([1, 5, 6, 4, 3, 2]))

main()
