from heapq import *


class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        return self.end < other.end

def find_max_cpu_load(jobs):
    jobs.sort(key=lambda x: x.start)
    maxLoad = 0
    currentLoad = 0
    minHeap = []

    for job in jobs:
        # NOTE: the head of the min heap is the meeting with the earliest end time
        # remove all mettings in the heap which have ended 
        while len(minHeap) > 0 and job.start >= minHeap[0].end:
            currentLoad -= minHeap[0].cpu_load
            heappop(minHeap)
        # add the current job
        heappush(minHeap, job)
        currentLoad += job.cpu_load
        # take a snapshot of current load against maxLoad seen so far
        maxLoad = max(maxLoad, currentLoad)
    return maxLoad


def main():
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))


main()
