# ====================================
# Find Concatenated Words As Substring
# ====================================


# Problem Statement
# ^^^^^^^^^^^^^^^^^
# Given a string and a list of words, find all the starting indices of substrings 
# in the given string that are a concatenation of all the given words exactly once 
# without any overlapping of words. It is given that all words are of the same length.

def find_word_concatenation(str, words):
    resultIndices = [] # return this at the end
    windowStart, windowEnd = 0, 0 
    wordLen = len(words[0]) # length of each word in words
    wordMap ={} # hold all words we've seen thus far in this map
    
    # iterate through the string 
    while(windowEnd < len(str) - wordLen + 1):
        nextWord = str[windowEnd : windowEnd + wordLen]
        print(windowEnd)

        # if the next 3 letters are a wanted word
        #   and not in the wordMap
        #       add them into the WordMap
        #   are in the word map
        #       update wordmap and windowStart to windowEnd
        if nextWord in words:
            if nextWord not in wordMap:
                wordMap[nextWord] = 0
            wordMap[nextWord] += 1 
            while(wordMap[nextWord] > 1): 
                leftWord = str[windowStart : windowStart + wordLen]
                if leftWord in words:
                    wordMap[leftWord] -= 1
                    if wordMap[leftWord] == 0:
                        del wordMap[leftWord]
                    windowStart += wordLen
            
        # if the next 3 letters are not a wanted word
        #   clear wordMap
        #   set windowStart to windowEnd
        if nextWord not in words:
            wordMap.clear()
            windowStart = windowEnd + wordLen

        # if we have a concatenation of all wanted words in our windows
        # # (if len(wordMap) == len(words))
        #   then mark index (windowStart) 
        if len(wordMap) == len(words):
            resultIndices.append(windowStart)

        windowEnd += wordLen
    
    return resultIndices

def main():
  print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
  print()
  print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))

main()