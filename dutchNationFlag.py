# ===========================
# Dutch National Flag Problem
# ===========================

# PROBLEM STATEMENT
# Given an array containing 0s, 1s and 2s, sort the array in-place. 
# You should treat numbers of the array as objects, hence, we can’t 
# count 0s, 1s, and 2s to recreate the array.

# The flag of the Netherlands consists of three colors: red, white 
# and blue; and since our input array also consists of three different 
# numbers that is why it is called Dutch National Flag problem.

def dutch_flag_sort(arr):
    pointer = 0
    low, high = 0, len(arr) - 1

    # when pointer reaches high index, we've sorted
    while pointer <= high:
        # if current pointer value is 0
        # switch pointer value with low value
        # increment low index, pointer 
        if arr[pointer] == 0:
            arr[low], arr[pointer] = arr[pointer], arr[low]
            pointer += 1 # shift pointer to the right since when solidifying a low value
            low += 1
        # if current pointer value is 1
        # increment pointer
        elif arr[pointer] == 1:
            pointer += 1
        # if current pointer value is 2
        # switch pointer value with high value
        # decrement high index
        else:
            arr[pointer], arr[high] = arr[high], arr[pointer]
            high -= 1
    return arr

def main():
  arr = [1, 0, 2, 1, 0]
  dutch_flag_sort(arr)
  print(arr)

  arr = [2, 2, 0, 1, 2, 0]
  dutch_flag_sort(arr)
  print(arr)


main()