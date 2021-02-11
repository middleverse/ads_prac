from heapq import *

def sort_character_by_frequency(str):
    reprogrammed_string = ''
    frequency_map = dict()
    
    # build a hashmap with frequence of each string    
    for i in range(len(str)):
        frequency_map[str[i]] = frequency_map.get(str[i], 0) + 1

    # insert all into max_heap
    max_heap = []
    for key in frequency_map:
        heappush(max_heap, (-frequency_map[key], key))
    
    # build reprogrammed string, top of heap is always next more frequent char
    while max_heap:
        frequency, char = heappop(max_heap)
        reprogrammed_string += char * -frequency
    
    return reprogrammed_string


def main():

  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()
