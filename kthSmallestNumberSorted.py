from heapq import *

def find_Kth_smallest(lists, k):
    number, count = -1, 0

    merged, min_heap = [], []

    # insert first element of each list into min heap
    for i in range(len(lists)):
        l = lists[i]
        if len(l) > 0:
            heappush(min_heap, (l[0], i))
            del l[0]
            
    # insert the minimum element (top element of heap) into merged list
    # this current element that was inserted is associated with a list
    # if that list still has elements, insert that element into min heap
    while min_heap and count < k:
        count += 1
        el, lidx = heappop(min_heap)
        merged.append(el) # add to merged list
        if len(lists[lidx]) > 0:
            heappush(min_heap, (lists[lidx][0], lidx))
            del lists[lidx][0]
    
    print(merged)
    # k'th smallest element will be last element in merged list
    number = merged[-1]
    return number


def main():
    print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))
    print("Kth smallest number is: " +
        str(find_Kth_smallest([[5, 8, 9], [1, 7]], 3)))
        



main()
