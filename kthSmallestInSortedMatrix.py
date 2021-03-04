from heapq import *

def find_Kth_smallest(matrix, k):
    number, count = -1, 0

    min_heap = []

    # insert first element of each row onto heap
    for i in range(len(matrix)):
        row = matrix[i]
        heappush(min_heap, (row[0], i))
        del row[0]

    # pop top of heap (min element), update counter
    # stop while loop when we're on our k'th number
    # otherwise if the list that is associated with currently popped number
    # has a next element, push it onto heap
    while min_heap and count < k:
        count += 1
        number, ridx = heappop(min_heap)
        if matrix[ridx]:
            heappush(min_heap, (matrix[ridx][0], ridx))
            del matrix[ridx][0]
               
    return number


def main():
    print("Kth smallest number is: " +
            str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()
