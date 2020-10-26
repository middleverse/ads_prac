# ===========================================
# Find Smallest Contiguous Subarray Given Sum
# ===========================================

import math

def smallest_subarray_with_given_sum(s, arr):
    windowStart, windowEnd = 0, 0
    minSubSize = math.inf # initialize to higest possible positive value
    windowSum = 0

    # loop ends when windowEnd reaches last element
    for windowEnd in range(len(arr)):
        # add next element to sum
        windowSum += arr[windowEnd]
        
        # while windowSum is >= s keep making window smaller from the left
        # by pushing windowStart to the right
        # if the windowSum is still >=s we know we're finding smaller subsets
        # that still add up to s or more
        while windowSum >= s:
            # if there is a new minimum value of subset size, choose that
            minSubSize = min(minSubSize, windowEnd - windowStart + 1)
            # remove left most value from windowSum
            windowSum -= arr[windowStart]
            # push right
            windowStart += 1
    # if no subset add up to s, return 0
    if minSubSize == math.inf:
        return 0
    # found a subset that adds up to s
    return minSubSize

def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))
    
# if not imported as a module, call main()
if __name__ == "__main__":
    main();

