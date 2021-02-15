from heapq import *

def find_maximum_distinct_elements(nums, k):
    frequency_map = {}
    min_heap = [] # min heap sorted of element frequency, format: (element frequency, element)

    # build the frequency map
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1
    
    # build the min heap
    for key in frequency_map:
        if frequency_map[key] > 1:
            heappush(min_heap, (frequency_map[key], key))

    # unique count before deletion process is all distinct elements 
    # minus the number of elements that have frequency higher than 1
    unique_count = len(frequency_map) - len(min_heap)

    while k > 0 and len(min_heap) > 0:
        current_element_frequency, current_element = heappop(min_heap)
        while current_element_frequency > 1 and k > 0:
            k -= 1
            current_element_frequency -= 1
        
        if current_element_frequency == 1:
            unique_count += 1
    
    # if all elements left are now distinct but we still have
    # a requirement to delete more elements due to size of k
    # delete any distinct elements
    while k > 0:
        unique_count -= 1
        k -= 1

    return unique_count


def main():

  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()

