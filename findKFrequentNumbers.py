from heapq import *

def find_k_frequent_numbers(nums, k):
    topNumbers = []
    frequency_map = dict()
    min_heap = [] 

    # build hash map of frequencies of each num
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    # build a min heap of size k, iterate through all nums
    # if num is > top of min heap, pop the top and insert num
    # when the iteration of nums is over, we're left with the
    # more frequent K elems
    for key in frequency_map:
        # if we don't have k elements in min heap, push
        if len(min_heap) < k:
            heappush(min_heap, (frequency_map[key], key))
        # if the top of min heap is less than current elements frequency, push
        elif frequency_map[key] > min_heap[0][0]:
            heappop(min_heap)
            heappush(min_heap, (frequency_map[key], key))
    
    while min_heap:
        frequency, element = heappop(min_heap)
        topNumbers.append(element)
    return topNumbers


def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11, 1, 11, 3, 8, 4, 5, 5, 6, 6, 6, 6], 3)))

main()

