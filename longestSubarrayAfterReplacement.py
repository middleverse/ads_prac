# ===========================================
# Longest Substring w/ Ones After Replacement
# ===========================================

# Problem Statement
# ^^^^^^^^^^^^^^^^^
# Given an array containing 0s and 1s, if you are allowed to 
# replace no more than ‘k’ 0s with 1s, find the length of the 
# longest contiguous subarray having all 1s.
# Ex: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2, Output: 6

def length_of_longest_substring(arr, k):
    windowStart = 0
    maxSubarrayLen = 0
    digitFreq = {}

    # iterate over all digits
    for windowEnd in range(len(arr)):
        nextDigit = arr[windowEnd]
        # add next digit to window
        if nextDigit not in digitFreq:
            digitFreq[nextDigit] = 0
        # update digitFrequecy table
        digitFreq[nextDigit] += 1

        # after adding new rightmost digit
        # if more than k zeroes in our window,
        # shift window start right until we have k zeroes
        while digitFreq[0] > k:
            digitFreq[arr[windowStart]] -= 1
            windowStart += 1

        # recalculate max window size seen till now
        maxSubarrayLen = max(maxSubarrayLen, windowEnd - windowStart + 1)
    return maxSubarrayLen
    
def main():
    print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))

main()