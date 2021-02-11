from collections import deque
from collections import deque
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        queue = deque()
        cities_seen = dict()
        total_city_count = 0
        province_count = 0
        # build dict of cities
        for city_id in range(len(isConnected)):
            cities_seen[city_id] = False
        # calculate total provinces    
        for i in range(len(isConnected)):
            # append city to queue only if haven't encountered it before 
            # otherwise it's already included in a province, 
            # in that case increment i
            if cities_seen[i] == False:
                queue.append(i)
                province_count += 1
            else:
                continue
            # append any cities that the current city is connected with 
            # to the queue, from there find all connected cities to 
            # cities that are continously added to the queue
            # once the queue is empty, we know we've covered a province
            while queue:
                total_city_count += 1
                row_index = queue.popleft()
                for j in range(len(isConnected[row_index])):
                    if isConnected[row_index][j] == 1:
                        cities_seen[j] = True
                        isConnected[row_index][j] = 0
                        isConnected[j][row_index] = 0
                        queue.append(j)
        return province_count


def main():
    s = Solution()
    print(s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))


main()