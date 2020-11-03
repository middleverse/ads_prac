# =================================================== 
# Longest Substring w/ Same Letters After Replacement
# ===================================================

# Problem Statement
# ^^^^^^^^^^^^^^^^^
# Given a string with lowercase letters only, if you are allowed 
# to replace no more than ‘k’ letters with any letter, find the length 
# of the longest substring having the same letters after replacement.
# Ex: Input: "aabccbb", k=2, Output: 5 (replacing 'cc' with 'bb' produces 'bbbbb')

charMap = {} # character frequency map 

# helper function that returns the frequency sum of all chars 
# but the one with highest recurring frequency
def calculateLowerFreqSum():
    maxFreq = 0
    total = 0
    for value in charMap.values():
        total += value
        maxFreq = max(maxFreq, value)
    return total - maxFreq
        


# return the longest substring that solves the problem statement
def length_of_longest_substring(str, k):
    charMap.clear()
    windowStart = 0
    maxSubstringLen = 0

    # iterator over string
    for windowEnd in range(len(str)):
        nextChar = str[windowEnd]
        if nextChar not in charMap:
            charMap[nextChar] = 0
        charMap[nextChar] += 1

        # iterate through str
        # if window doesn't meet certain critera, shift windowStart right
        while calculateLowerFreqSum() > k:
            startChar = str[windowStart]
            # print(startChar)
            # update charMap based on window shift
            charMap[startChar] -= 1
            if charMap[startChar] == 0:
                del charMap[startChar]
            windowStart += 1
        # update max
        maxSubstringLen = max(maxSubstringLen, windowEnd - windowStart + 1)
        # print(maxSubstringLen)
    # return int value
    return maxSubstringLen


def main():
  print(length_of_longest_substring("aabccbb", 2))
  print(length_of_longest_substring("abbcb", 1))
  print(length_of_longest_substring("abccde", 1))

main()

