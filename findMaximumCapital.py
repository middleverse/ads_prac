from collections import deque

def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    current_capital, i = initialCapital, 1
    
    while numberOfProjects:
        # push capital amounts on top of deque until we find a capital that we can't afford yet
        # top of deque now will be our next investment amount
        while i < len(profits) and current_capital >= capital[i]:
            i += 1
        
        current_capital += profits[i-1] 
        numberOfProjects -= 1

    return current_capital


def main():
  print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
  print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))

main()
