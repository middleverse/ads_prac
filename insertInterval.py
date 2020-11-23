# ===============
# Insert Inverval
# ===============

# Problem Statement 
# Given a list of non-overlapping intervals sorted by their start time, 
# insert a given interval at the correct position and merge all 
# necessary intervals to produce a list that has only mutually exclusive 
# intervals.

def insert(intervals, new_interval):
    start, end = new_interval[0], new_interval[1]
    merged = []
    i = 0
    
    # skip and append all intervals whos end is less than new interval start
    while i < len(intervals) and intervals[i][1] < start:
        merged.append(intervals[i])
        i += 1

    # skip over all intervals where who's start is less then new interval end 
    # figure out overlap and insert
    while i < len(intervals) and intervals[i][0] <= end:
        start = min(intervals[i][0], start)
        end = max(intervals[i][1], end)
        i += 1
    merged.append([start, end])

    # insert rest of the intervals
    while (i < len(intervals)):
        merged.append(intervals[i])
        i += 1
    return merged


def main():
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()
