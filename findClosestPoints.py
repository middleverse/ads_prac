import math
from heapq import *

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def print_point(self):
    print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

def euclidean_distance(point):
    return point.x * point.x + point.y * point.y

def find_closest_points(points, k):
    result = []
    max_heap = [] # each elem => [e_distance][index]

    # insert first k points' index and their euclidean distance into max_heap
    # max heap will be sort on euclidean distance
    for i in range(k):
        heappush(max_heap, (-euclidean_distance(points[i]), i))
    
    for j in range(k, len(points)):
        current_distance = euclidean_distance(points[j])
        if current_distance < -max_heap[0][0]:
            heappop(max_heap)
            heappush(max_heap, (-current_distance, j))

    for p in range(k):
        distance, index = heappop(max_heap)
        result.append(points[index])
    return result


def main():

  result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()


main()