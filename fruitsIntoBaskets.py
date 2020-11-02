# ====================
# Fruit Basket Problem
# ====================

# Problem Statement
# ^^^^^^^^^^^^^^^^^
# Given an array of characters where each character represents 
# a fruit tree, you are given two baskets and your goal is to 
# put maximum number of fruits in each basket. The only restriction
# is that each basket can have only one type of fruit.
# NOTE: You can start with any tree, but once you have started you
# can't skip a tree. So you'll have to stop when picking from a 
# third tree.


def fruits_into_baskets(fruits):
    startWindow, endWindow = 0, 0
    characterMap = {} # HashMap used to track character in window
    maxFruitsPicked = 0

    # go over list of symbols
    for endWindow in range(len(fruits)):
        currentSymbol = fruits[endWindow]
        
        # if the new fruit encountered is distinct
        if currentSymbol not in characterMap:
            # shift startWindow to the right, until one basket is empty
            # which is the same as when characterMap is 1
            while(len(characterMap) > 1):
                startSymbol = fruits[startWindow]
                # decrement startSymbol count by 1 (shifting right)
                characterMap[startSymbol] -= 1
                # if there is no fruit of this symbol left in the window
                # delete symbol from character map
                if characterMap[startSymbol] == 0:
                    del characterMap[startSymbol]
                # shift start window to the right 
                startWindow += 1
            # add next symbol
            characterMap[currentSymbol] = 0

        # add current symbol to basket
        characterMap[currentSymbol] += 1        
        
        # keep track of max window size (largest sum of fruits)
        windowLen = endWindow - startWindow + 1
        maxFruitsPicked = max(maxFruitsPicked, windowLen)

    return maxFruitsPicked

def main():
    a = fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])
    b = fruits_into_baskets(['C', 'B', 'B', 'C', 'A', 'B'])
    print (a)
    print (b)

if __name__ == '__main__':
    main()