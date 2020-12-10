# =======================
# Find Duplicate In Place
# =======================

# PROBLEM STATEMENT
# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. 
# The array has only one duplicate but it can be repeated multiple times. Find that 
# duplicate number without using any extra space. You are, however, allowed to modify 
# the input array.

def find_duplicate(nums):

    # iterate from 1 to n
    #   move to next index if current index matches its elements (i = nums[i] - 1)
    #   if it doesn't match:
    #       if element at i is the same as element at nums[i] - 1: 
    #           we found the duplicate
    #       else:
    #           switch element at i with element at index nums[i] - 1
    #   

    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            correctIndex = nums[i] - 1
            # found duplicate
            if nums[i] == nums[correctIndex]:
                return nums[i]
            else:
                nums[i], nums[correctIndex] = nums[correctIndex], nums[i]        
        else:
            i += 1
    # couldn't find duplicate
    return -1

def main():
    print(find_duplicate([1, 4, 4, 3, 2]))
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    print(find_duplicate([2, 3, 1, 5, 4]))

main()
