from heapq import *

def find_sum_of_elements(nums, k1, k2):
    max_heap = []

    for i in range(k2):
        heappush(max_heap, -nums[i])
    # if the top of the heap is greater than current element, pop top and push element
    for i in range(k2, len(nums)):
        if nums[i] < -max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])
            
    sum, elem = 0, 0
    sum -= -max_heap[0]
    for _ in range(k2 - k1 + 1):
        elem = -heappop(max_heap)
        sum += elem
    sum -= elem

    return sum   


def main():

  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()
