from heapq import *

def find_k_largest_numbers(nums, k):
    min_heap = []
    # if heap size is smaller than k, insert first k elements
    for i in range(k):
        heappush(min_heap, nums[i])

    for j in range(k, len(nums)):
        if nums[j] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, nums[j])

    return min_heap


def main():

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()

