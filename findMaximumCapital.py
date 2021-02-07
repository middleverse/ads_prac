from heapq import * 

def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    min_capital_heap = [] # default heapq is min heap
    max_profit_heap = [] # remember to push - numbers to make this a max heap

    # create min heap with project capitals and their index
    for i in range(len(profits)):
        heappush(min_capital_heap, (capital[i], i))
    
    # find the best projects (total of "numberOfProjects")
    current_capital = initialCapital
    for _ in range(numberOfProjects):
        # select all project that can be afforded currently and insert into max_profit_heap
        while min_capital_heap and min_capital_heap[0][0] <= current_capital:
            capital, i = heappop(min_capital_heap)
            heappush(max_profit_heap, (-profits[i], i)) # biggest profits will rise to the top
        
        # if we couldn't find anything we can currently afford, break
        if not max_profit_heap:
            break

        # add the max profit we can afford to our current capital
        current_capital += -heappop(max_profit_heap)[0]

    return current_capital

def main():
  print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2], [1, 2, 3], 1, 1)))
  print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))

main()
