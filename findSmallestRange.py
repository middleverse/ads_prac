from heapq import *
import math

def find_smallest_range(lists):
    min_heap = []


    left, right = 0, math.inf
    current_max_number = -math.inf
    
    # push first element of all lists onto heap
    for l in lists:
        heappush(min_heap, (l[0], 0, l))
        current_max_number = max(l[0], current_max_number)

    # pop the heap on start
    # the min element now becomes what pops out of the heap
    # if the range between current max and current min (num) and smaller
    #   than what's seen so far (right - left), update right and left
    while len(min_heap) == len(lists):
        num, idx, arr = heappop(min_heap)
        if right - left > current_max_number - num:
            left = num
            right = current_max_number
        if idx + 1 < len(arr):
            idx += 1
            heappush(min_heap, (arr[idx], idx, arr))
            # update current max, right will always be last current_max_number
            current_max_number = max(arr[idx], current_max_number)

    return[left, right]    
    


def main():
    print("Smallest range is: " +
            str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))
    print("Smallest range is: " +
            str(find_smallest_range([[1, 9], [4, 12], [7, 10, 16]])))

main()

