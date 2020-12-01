# ============================
# Minimum Meeting Rooms (hard) 
# ============================
#
# PROBLEM STATEMENT
# Given a list of intervals representing the start and end time of ‘N’ meetings, 
# find the minimum number of rooms required to hold all the meetings.
#
# EXAMPLE
# Meetings: [[4,5], [2,3], [2,4], [3,5]]
# Output: 2
# Explanation: We will need one room for [2,3] and [3,5], 
# and another room for [2,4] and [4,5].
from heapq import *

class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.end < other.end


def min_meeting_rooms(meetings):
    # sort the meetings by start time
    meetings.sort(key=lambda x: x.start)

    minRooms = 0
    minHeap = []
    for m in meetings:
        # NOTE: the meeting that started earliest in the heap will be the root
        # remove all the meetings that have ended before meeting m
        while len(minHeap) > 0 and m.start >= minHeap[0].end:
            heappop(minHeap)
        # add the current meeting to heap
        heappush(minHeap, m)
        # the heap now contains all active meetings,
        # take a snapshot to see current size of heap is greater than minRooms
        minRooms = max(len(minHeap), minRooms)
    return minRooms


def main():
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
        [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
    print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
    print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
    print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))


main()
