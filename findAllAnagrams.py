# ====================
# Anagrams In A String
# ====================

# Problem Statement
# ^^^^^^^^^^^^^^^^^
# Given a string and a pattern, find all anagrams of the pattern 
# in the given string. Write a function to return a list of starting 
# indices of the anagrams of the pattern in the given string.
# NOTE: Assume all distinct characters in pattern

# return True if all anagrams of pattern found, False otherwise
def findStringAnagrams(str, pattern):
    windowStart, numberOfAnagrams = 0, 0
    anagramTable = {}
    anagramIndices = []
    charBalance = {}

    # build a hashmap that contains the balance of each distinct character
    for pchar in pattern:
        charBalance[pchar] = 1
        
    # iterate over all characters in string to form a window
    # if nextChar is not a permutation character,
    # then shift start window right to 1 past the end window
    # if nextChar is a permutation character and balance goes 
    # below 0 once added to map, then shift start window right 
    # until nextChar balance is restored to 0
    for windowEnd in range(len(str)):
        nextChar = str[windowEnd]

        # if nextChar is a pattern character
        if nextChar in charBalance:
            charBalance[nextChar] -=1
            # shift window right
            while charBalance[nextChar] < 0:
                charBalance[str[windowStart]] += 1
                windowStart += 1
        # if nextChar is not a pattern
        else:
            while(windowStart <= windowEnd):
                if str[windowStart] in charBalance:
                    charBalance[str[windowStart]] += 1
                windowStart += 1

        # if this window is a permutation:
        #   add it to the anagram table if not already added       
        if windowEnd - windowStart + 1 == len(pattern):
            currentAnagram = str[windowStart:windowEnd + 1]
            if currentAnagram not in anagramTable:
                anagramTable[currentAnagram] = None
                anagramIndices.append(windowStart)

    return anagramIndices

def main():
    print(findStringAnagrams("ppqp", "pq"))
    print(findStringAnagrams("abbcabc", "abc"))

main()
