from heapq import *


def find_closest_elements(arr, K, X):
    max_heap = []
    
    # iterate through all nums
    for i in range(len(arr)):
        current_element_distance = arr[i] - X
        if current_element_distance < 0:
            current_element_distance *= -1

        # populate heap with first K elements
        if len(max_heap) < K:
            heappush(max_heap, (-current_element_distance, i))
        
        # if current distance is closer to X than top of heap, remove top and insert current element
        elif current_element_distance < -max_heap[0][0]:
            heappop(max_heap)
            heappush(max_heap, (-current_element_distance, i))

    min_index = K
    # we'll have a heap of K elements closest to X
    # pop each heap element and note down starting (min) index of the closes values
    while len(max_heap) > 0:
        distance, index = heappop(max_heap)
        min_index = min(index, min_index)

    return arr[min_index: min_index + K]


def main():
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
