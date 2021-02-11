from heapq import *

def minimum_cost_to_connect_ropes(ropeLengths):
    cost = 0
    min_heap = []
    for rope in ropeLengths:
        heappush(min_heap, rope)
    
    while len(min_heap) > 1:
        new_elem = heappop(min_heap) + heappop(min_heap)
        cost += new_elem
        heappush(min_heap, new_elem)

    return cost


def main():

  print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()

