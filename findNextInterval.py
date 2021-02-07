from heapq import *

class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end


def find_next_interval(intervals):
    # create two max heaps
    max_start_heap = []
    max_end_heap = []
    n = len(intervals)
    result = [0 for i in range(n)]

    # populate heaps
    for index in range(n):
        heappush(max_end_heap, (-intervals[index].end, index))
        heappush(max_start_heap, (-intervals[index].start, index))

    # find a next interval for each interval
    for _ in range(n):
        # find next interval for interval with max end in end_heap
        top_end, top_end_index = heappop(max_end_heap) # top end value is negative here, keep in mind
        result[top_end_index] = -1 # default
        
        # if we find an interval with interval start >= top_end interval end, we found a next interval
        if -max_start_heap[0][0] >= -top_end:
            top_start, top_start_index = heappop(max_start_heap)
            while max_start_heap and -max_start_heap[0][0] >= -top_end:
                top_start, top_start_index = heappop(max_start_heap)
            result[top_end_index] = top_start_index
            heappush(max_start_heap, (top_start, top_start_index))
        # else there is no next interval, do nothing

    return result


def main():

  result = find_next_interval(
    [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
  print("Next interval indices are: " + str(result))

  result = find_next_interval(
    [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
  print("Next interval indices are: " + str(result))


main()
