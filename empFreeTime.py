# ========================
# Employee Free Time (hard) 
# ========================

# PROBLEM STATEMENT
# For ‘K’ employees, we are given a list of intervals representing the 
# working hours of each employee. Our goal is to find out if there is a 
# free interval that is common to all employees. You can assume that each 
# list of employee working hours is sorted on the start time.


from __future__ import print_function
from heapq import *

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

class EmployeeInterval:
    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval # interval repping employees work hours
        self.employeeIndex = employeeIndex # index of employee's list of hours in schedule
        self.intervalIndex = intervalIndex # index of this interval in the employee's list

    def __lt__(self, other):
        # we'll compare end explicitly in code later
        return self.interval.start < other.interval.start

def find_employee_free_time(schedule):
    result, minHeap = [], []
    if schedule is None: return []

    # push first interval of each employee on to the heap
    workers = len(schedule)
    for w in range(workers):
        heappush(minHeap, EmployeeInterval(schedule[w][0], w, 0)) # heap sorted on interval.start

    previousInterval = minHeap[0].interval # keep track of previous interval compared

    # iterate over all employee lists in schedule
    # when minHeap is empty, we know we've compared all of them
    while minHeap:
        queueHead = heappop(minHeap)
        # if previousInternal is not overlapping with the next interval, insert a free interval
        if previousInterval.end < queueHead.interval.start:
            result.append(Interval(previousInterval.end, queueHead.interval.start))
            previousInterval = queueHead.interval
        
        # we have overlapping intervals, update the previousInternal if queueHead ends after it
        else:
            if previousInterval.end < queueHead.interval.end:
                previousInterval = queueHead.interval
        
        # if there are more intervals available for next employee, add it to heap
        employeeSchedule = schedule[queueHead.employeeIndex]
        if len(employeeSchedule) > queueHead.intervalIndex + 1:
            heappush(minHeap, EmployeeInterval(employeeSchedule[queueHead.intervalIndex + 1], 
                                                queueHead.employeeIndex, queueHead.intervalIndex + 1))
    return result

def main():

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()
