from heapq import *

def find_smallest_range(lists):
    merged_idxs, merged_nums, min_heap = [], [], []
    n = len(lists)

    # push first element of all lists onto heap
    for i in range(len(lists)):
        l = lists[i]
        heappush(min_heap, (l[0], i))
        del l[0]

    # when heap is empty, we know all elements of all lists have been merged
    while min_heap:
        el, lidx = heappop(min_heap)
        merged_idxs.append(lidx)
        merged_nums.append(el)
        if lists[lidx]:
            heappush(min_heap, (lists[lidx][0], lidx))
            del lists[lidx][0]

    # we now have ONE merged sorted list of all elements
    num_freq = dict()

    left, right = 0, -1
    result = [merged_nums[0], merged_nums[-1] ]
    while right < n - 1: # push n - 1 numbers on to the freq_char
        right += 1
        num_freq[merged_idxs[right]] = num_freq.get(merged_idxs[right], 0) + 1

    # drive right all the way through the merged list of nums
    while right < len(merged_idxs) - 1:
        if len(num_freq) == n: # if we have one num from each list 
            if merged_nums[right] - merged_nums[left] < result[1] - result[0]:
                result = [merged_nums[left], merged_nums[right]]
            # update variables & num_freq as we move left to the right by one index
            num_freq[merged_idxs[left]] -= 1
            if num_freq[merged_idxs[left]] <= 0:
                del num_freq[merged_idxs[left]]
            left += 1
        else:
            right += 1
            num_freq[merged_idxs[right]] = num_freq.get(merged_idxs[right], 0) + 1

    return result


def main():
    print("Smallest range is: " +
            str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))
    print("Smallest range is: " +
            str(find_smallest_range([[1, 9], [4, 12], [7, 10, 16]])))

main()

