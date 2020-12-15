# ============================
# Find All Duplicates In Place
# ============================

# PROBLEM STATEMENT
# We are given an unsorted array containing ‘n’ numbers taken from 
# the range 1 to ‘n’. The array has some numbers appearing twice, 
# find all these duplicate numbers without using any extra space.

def find_all_duplicates(nums):
    duplicateNumbers = []
    
    # try to move element at current index to it's correct position
    # if already at correct position, increment index
    # if element at correct position is of the same value,
    #   add to duplicate list
    #   increment index
    # else
    #   switch elements

    i = 0
    while i < len(nums):
        correct_index = nums[i] - 1
        if nums[correct_index] == nums[i]:
            i += 1
        else:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]

    for j in range(len(nums)):
        if nums[j] != j + 1:
            duplicateNumbers.append(nums[j])
    
    return duplicateNumbers

def main():
  print(find_all_duplicates([3, 4, 4, 5, 5]))
  print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))

main()