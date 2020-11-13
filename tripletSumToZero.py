# ===========================
# Unique Triplets Sum To Zero
# ===========================

# PROBLEM STATEMENT
# Given an array of unsorted numbers, 
# find all unique triplets in it that add up to zero.
# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# Explanation: There are four unique triplets whose sum is equal to zero.

def search_duplet(arr, target_sum, left, triplets):
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        # if we've found left and right that add to target_sum
        # append a combination to triplets
        # then shift left and right appropriately
        # subsequently handle duplicates
        if current_sum == target_sum:
            triplets.append([-target_sum, arr[left], arr[right]])

            # both right and left elements have been used in this triplet
            # so either one can't be used again with the current target sum
            # since if left is used with target sum the only answer is right
            # and same with right being used with target sum, the only value
            # that makes a triplet with those two is left. Hence we shift
            # left index to the right and right index to the left
            left += 1
            right -= 1 
            
            # handle duplicates on either side
            while left < right and arr[left] == arr[left - 1]:
                left += 1 # skip duplicate element
            while left < right and arr[right] == arr[right + 1]:
                right -= 1 # skip duplicate element

        # target sum is still greater than current sum
        elif target_sum > current_sum:
            left += 1

        # target sum is less than current sum
        else:
            right -= 1


def search_triplets(arr):
    triplets = []
    arr.sort()
    
    # iterate through all elements in arr
    # use that as a potential target sum
    # and search for a pair that sums with 
    # current element - to zero (found triplet)
    for index in range(len(arr)):
        if index > 0 and arr[index] == arr[index - 1]:
            continue # this is a duplicate, skip
        # find a pair that completes a triplet
        # use 
        search_duplet(arr, -arr[index], index + 1, triplets)
    return triplets

def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))


main()