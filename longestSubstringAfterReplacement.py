# =================================================== 
# Longest Substring w/ Same Letters After Replacement
# ===================================================

# Problem Statement
# ^^^^^^^^^^^^^^^^^
# Given a string with lowercase letters only, if you are allowed 
# to replace no more than ‘k’ letters with any letter, find the length 
# of the longest substring having the same letters after replacement.
# Ex: Input: "aabccbb", k=2, Output: 5 (replacing 'cc' with 'bb' produces 'bbbbb')
     
# return the longest substring that solves the problem statement
def length_of_longest_substring(str, k):
    charMap = {}
    windowStart = 0
    maxSubstringLen, maxRepeatCharFreq = 0, 0

    # iterator over string
    for windowEnd in range(len(str)):
        nextChar = str[windowEnd]
        if nextChar not in charMap:
            charMap[nextChar] = 0
        charMap[nextChar] += 1
        maxRepeatCharFreq = max(maxRepeatCharFreq, charMap[nextChar])

        # iterate through str
        # if window doesn't meet certain critera, shift windowStart right
        while windowEnd- windowStart + 1 - maxRepeatCharFreq > k:
            startChar = str[windowStart]
            # update charMap based on window shift
            charMap[startChar] -= 1
            windowStart += 1
        # update max
        maxSubstringLen = max(maxSubstringLen, windowEnd - windowStart + 1)
    # return int value
    return maxSubstringLen


def main():
  print(length_of_longest_substring("bbccbaa", 2))
  print(length_of_longest_substring("abbcb", 1))
  print(length_of_longest_substring("abccde", 1))

main()

