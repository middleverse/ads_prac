# ============================
# Find Max Contiguous Subarray
# ============================

# return max subarray size only
def max_sub_array_of_size_k(k, arr):
    windowStart, windowSum, maxSum = 0, 0, 0

    # windowEnd iterates for [0,..,n-1] where n is size of array
    for windowEnd in range(len(arr)):
        # add next element
        windowSum += arr[windowEnd]
        # slide window right by 1 && calculate new windowSum
        # for the first few iterations -> until windowEnd < k - 1, logic
        # doesn't enter if statement, enters for every iteration thereafter
        if windowEnd >= k - 1:
            # choose between previous max sum vs current window sum
            maxSum = max(maxSum, windowSum)
            # subtract the element going out
            windowSum -= arr[windowStart] 
            # point window start to next element
            windowStart += 1
    return maxSum

def main():
    k1, k2 = 2, 7 # subarray sizes
    arr1 = [2, 1, 5, 10, 4, 6, 11]
    arr2 = [1, 2, 3, 4, 5, 6, 7]
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(k1, arr1)))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(k2, arr2)))    
        
# if not imported as a module, run main
if __name__ == '__main__':
    main()