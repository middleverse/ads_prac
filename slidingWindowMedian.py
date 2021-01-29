from heapq import *
import heapq

class SlidingWindowMedian:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def find_sliding_window_median(self, nums, k):
        result = [0.0 for x in range(len(nums) - k + 1)]
        for i in range(0, len(nums)):
            # insert new num into heap
            if not self.maxHeap or nums[i] <= -self.maxHeap[0]:
                heappush(self.maxHeap, -nums[i])
            else:
                heappush(self.minHeap, nums[i])
            self.rebalance_heaps()
            # if we have atleast k elements in sliding window
            # add the median of current window
            if i + 1 - k >= 0:
                if len(self.minHeap) == len(self.maxHeap):
                    result[i + 1 - k] = (-self.maxHeap[0] + self.minHeap[0]) / 2.0
                else:
                    result[i + 1 - k] = -self.maxHeap[0] / 1.0
                # remove first element in window
                start_of_window_index = i - k + 1
                element_to_be_removed = nums[start_of_window_index]
                if element_to_be_removed <= -self.maxHeap[0]:
                    self.remove_element(self.maxHeap, -element_to_be_removed)
                else:
                    self.remove_element(self.minHeap, element_to_be_removed)
                self.rebalance_heaps()
        return result

    def remove_element(self, heap, element):
        # find the element in either of the heaps and remove
        ind = heap.index(element)
        heap[ind] = heap[-1]
        del heap[-1]
        if ind < len(heap):
            heapq._siftup(heap, ind)

    def rebalance_heaps(self):
        if len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
        elif len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))

def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()
