# =====================
# Interval Intersection
# =====================

# Given two lists of intervals, find the intersection of these two lists. 
# Each list consists of disjoint intervals sorted on their start time.
# EXAMPLE
# Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
# Output: [5, 7], [9, 10]
# Explanation: The output list contains the common intervals between the two lists.

def merge(intervals_a, intervals_b):
    results = []
    start, end = 0, 1
    i, j = 0, 0
    # use interval 'b' as traversal interval
    while i < len(intervals_b) and j < len(intervals_a):
        
        # skip all intervals in 'a' that are less than current interval in 'b'
        while j < len(intervals_a) and intervals_b[i][start] > intervals_a[j][end]:
             j += 1
        
        # either we have an overlap, or curr interval in 'b' is less than curr interval in 'a'
        if intervals_b[i][end] < intervals_a[j][start]: # no overlap
            i += 1
        else: # overlap
            interval_start = max(intervals_a[j][start], intervals_b[i][start])
            interval_end = min(intervals_a[j][end], intervals_b[i][end])
            results.append([interval_start, interval_end])
            if intervals_b[i][end] > intervals_a[j][end]:
                j += 1
            else:
                i += 1
    return results


def main():
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12], [13, 14], [15, 16], [17, 18]], [[5, 10], [18, 20]])))


main()
