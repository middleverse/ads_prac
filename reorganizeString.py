from heapq import *
from collections import deque

def reorganize_string(str, k):
    reorganized_string = ''
    max_heap = []

    char_frequency = dict()

    # build a hash map of char frequencies in str
    for char in str:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    # build a max heap with format tuple(frequency, char)
    for key in char_frequency:
        heappush(max_heap, (-char_frequency[key], key))

    current_char_list = deque()
    while max_heap:
        # pop top k elements from the heap, push them to a list
        freq, char = heappop(max_heap)
        reorganized_string += char
        # add the current char to list of chars added in this round of "k" distinct adds
        current_char_list.append((freq + 1, char)) 

        if len(current_char_list) == k:
            freq, char = current_char_list.popleft()
            if freq < 0:
                heappush(max_heap,(freq, char))
    
    return reorganized_string if len(reorganized_string) == len(str) else ''


def main():
  print("Reorganized string: " + reorganize_string("mmpp", 2))
  print("Reorganized string: " + reorganize_string("Programming", 3))
  print("Reorganized string: " + reorganize_string("aab", 2))
  print("Reorganized string: " + reorganize_string("aapa", 3))


main()
