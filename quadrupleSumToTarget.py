# =======================
# QUADRUPLE SUM TO TARGET
# =======================

# PROBLEM STATEMENT
# Given an array of unsorted numbers and a target number, 
# find all unique quadruplets in it, whose sum is equal to the target number.

def search_quadruplets(arr, target):
    arr.sort() 
    quadruplets = []

    # iterate through all elements in array till the 4th last
    for first_index in range(len(arr) - 3):
        
        # if duplicate element, then possibilities have been considered, skipe
        if first_index > 0 and arr[first_index] == arr[first_index - 1]:
            continue
        search_triplets(arr, target, first_index, quadruplets)
    return quadruplets

def search_triplets(arr, target, first_of_quadruplet, quadruplets):
    # iterate through elements starting one beyond first_of_quadruplet to find a triplet
    for second_index in range(first_of_quadruplet + 1, len(arr) - 2):

        # if duplicate element, then possibilities have been considered, skip
        if second_index > first_of_quadruplet + 1 and arr[second_index] == arr[second_index - 1]:
            continue
        search_duplets(arr, target, second_index, first_of_quadruplet, quadruplets)

# find duplets that complete quadruplet to sum to target 
# given the first two values of the quadruplet
def search_duplets(arr, target, first_of_triplet, first_of_quadruplet, quadruplets):
    # initialize pointers
    left, right = first_of_triplet + 1, len(arr) - 1 

    # find a pair that completeds the quadruplet, adding up to the target sum
    while left < right:
        current_sum = arr[left] + arr[right] + arr[first_of_quadruplet] + arr[first_of_triplet]
        
        # found a quadruplet, add it to the list and move pointers
        if current_sum == target:
            temp_list = [arr[first_of_quadruplet], arr[first_of_triplet], arr[left], arr[right]]
            quadruplets.append(temp_list)
            left += 1
            right -= 1

            # check for duplicates
            while left < right and arr[left] == arr[left - 1]:
                left += 1 # avoid duplicates on left side
            while left < right and arr[right] == arr[right + 1]:
                right -= 1 # avoid duplicates on right side

        # current sum is below or above target sum, move pointers appropriately        
        elif current_sum < target:
            left += 1
        else:
            right -= 1

def main():
  print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
  print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()


