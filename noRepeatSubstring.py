# =========================== 
# No-Repeat Substring Problem
# ===========================

# Problem Statement
# ^^^^^^^^^^^^^^^^^
# Given a string, find the length of the longest substring 
# which has no repeating characters.
# Ex: "aabccbb", output: 3 => ["abc"]

def non_repeat_substring(str):
    maxWindowLen, windowStart, windowEnd = 0, 0, 0
    freqMap = {} # used to hold character frequency

    # go over each character in string
    for windowEnd in range(len(str)):
        nextChar = str[windowEnd] # newest, rightmost character
        
        if nextChar in freqMap:
            # keep shifting windowStart to the right until we don't
            # have nextChar present in the current window 
            while nextChar in freqMap:
                del freqMap[str[windowStart]]
                windowStart += 1
        
        # Add nextChar to freqMap, no value needed, 
        # just keep track of existence
        freqMap[nextChar] = None
        # recalculate max window size seen so far
        maxWindowLen = max(maxWindowLen, windowEnd - windowStart + 1)
    
    return maxWindowLen

def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))

main()