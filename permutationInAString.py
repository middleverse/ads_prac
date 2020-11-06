# =======================
# Permutation In A String
# =======================

# Problem Statement
# ^^^^^^^^^^^^^^^^^
# Given a string and a pattern, find out if the string 
# contains any permutation of the pattern.
# [Example]
# Input: String="oidbcaf", Pattern="abc"
# Output: true, bca is a permutation of abc

# return True if permutation of pattern found, False otherwise
def findPermutation(str, pattern):
    windowStart = 0

    charBalance = {}
    # build a hashmap that contains the balance of each distinct character
    # if 'a' occurs in pattern 2 times, the balance of 'a' is 2 at the start
    for pchar in pattern:
        if pchar not in charBalance:
            charBalance[pchar] = 0
        charBalance[pchar] += 1
    
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

        # if this window is a permutation, return True        
        if windowEnd - windowStart + 1 == len(pattern):
            return True

    return False

def main():
    print(findPermutation("oidbcaf", "abc"))
    print(findPermutation("odicf", "dc"))
    print(findPermutation("bcdxabcdy", "bcdyabcdx"))
    print(findPermutation("aaacb", "abc"))

main()