# ===============
# Merge Intervals
# ===============

# PROBLEM STATEMENT
# Given a list of intervals, merge all the overlapping intervals to produce 
# a list that has only mutually exclusive intervals.

from __future__ import print_function
import math

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
    merged = []
    if len(intervals) < 2:
        return intervals
    intervals.sort(key = lambda x: x.start)

    # 1. sort the intervals on the start time (done above)
    # 2. if 'a' (prev interval) overlaps 'b' (curr interval), merge them into 'c'
    # 3. append 'c' to merged list
    start = intervals[0].start
    end = intervals[0].end
    for i in range(1, len(intervals)):
        curr_interval = intervals[i]
        if curr_interval.start <= end:
            # append interval c to list with start = a.start and end = max(a.end, b.end)
            end = max(end, curr_interval.end)
        else:
            merged.append(Interval(start, end))
            start = curr_interval.start
            end = curr_interval.end
    merged.append(Interval(start, end)) # last interval doesn't get appended earlier, do it now
    return merged
    

def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()

main()