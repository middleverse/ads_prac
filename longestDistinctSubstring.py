# =====================================
# Longest Substring W/ Distinct K Chars
# =====================================

import string

# Problem Statement
# ^^^^^^^^^^^^^^^^^
# Given a string, find the length of the longest substring 
# in it with no more than K distinct characters.
# Ex: string = "araaci", for K = 2 output = "araa" => ('r' & 'a')
# Ex: string = "araaci", for K = 1 output = "aa" => ('a')

def longest_substring_with_k_distinct(str, k):
    windowStart, windowEnd = 0, 0 # initialize window 
    maxLength = 0; 
    charMap = {} # HashMap to be used for tracking character frequency

    # iterator over each character in str
    # windowEnd automatically shifts right each iteration
    for windowEnd in range(len(str)):
        # ASCII value of current str window end 
        rightChar = str[windowEnd]
        # update rightChar frequency in HashMap
        if rightChar not in charMap:
            charMap[rightChar] = 0
        charMap[rightChar] +=1
        
        # as we shift to the right, there can be a state in the logic
        # when there are more than K distinct chars in the window, so:
        # while no. of distinct characters in current substring
        # are more than k, shift leftChar to the right until they are == K
        # ex: if the 3 leftmost chars are all 'a', this loop runs thrice
        while len(charMap) > k:
            leftChar = str[windowStart]
            charMap[leftChar] -= 1
            # update leftChar in hashmap
            if charMap[leftChar] == 0:
                del charMap[leftChar]   
            # shift start of window left by 1
            windowStart += 1
        # update largest substring size
        maxLength = max(maxLength, windowEnd - windowStart + 1)
    return maxLength

def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("llllllll", 3)))

# if run directly
if __name__ == '__main__':
    main()