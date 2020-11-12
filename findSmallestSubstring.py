# ===============================
# Find Smallest Substring Problem
# ===============================

def find_substring(str, pattern):
    windowStart, smallestMatchWindow = 0, len(str) + 1
    smallestStr = ''
    countMap = {}

    # # assume all distinct chars in pattern
    # for char in pattern:
    #     countMap[char] = 1

    # iterate through chars in str to find smallest substring     
    for windowEnd in range(len(str)):
        nextChar = str[windowEnd] # char at windowEnd

        # 
        if nextChar in pattern:
            if nextChar not in countMap:
                countMap[nextChar] = 0
            countMap[nextChar] += 1 # update symbol count in window
        
        # trim window from the left if: 
        # windowStart points to a char not in pattern
        # or windowStart points to a char in patter that has been seen more than once
        while str[windowStart] not in pattern or countMap[str[windowStart]] > 1:
            if str[windowStart] in countMap:
                countMap[str[windowStart]] -= 1
            windowStart += 1
            
        # if pattern found in current window
        # check if this is the smallest window with match so far
        # and update smallestStr
        if len(countMap) == len(pattern): # this works as we've assumed all distinct chars in pattern
            if windowEnd - windowStart + 1 < smallestMatchWindow:
                smallestMatchWindow = windowEnd - windowStart + 1
                smallestStr = str[windowStart : windowEnd + 1]

    return smallestStr 


def main():
    print(find_substring("aabdec", "abc"))
    print(find_substring("abdbca", "abc"))
    print(find_substring("adcad", "abc"))

main()