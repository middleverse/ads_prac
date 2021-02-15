from heapq import *


def rearrange_string(str):

    max_heap = [] # format: (char frequency, char)
    char_frequency = dict()
    rearranged_str = ''

    for i in range(len(str)):
        char_frequency[str[i]] = char_frequency.get(str[i], 0) + 1

    # build a max heap 
    for key in char_frequency:
        if char_frequency[key] > (len(str) + 1) / 2:
            return ''
        heappush(max_heap, (-char_frequency[key], key))
    
    prev_char_tuple = None
    while len(rearranged_str) < len(str):
        frequency, char = heappop(max_heap)
        if prev_char_tuple:
            heappush(max_heap, prev_char_tuple)
        frequency += 1
        rearranged_str += char
        if frequency < 0:
            prev_char_tuple = (frequency, char)
        else:
            prev_char_tuple = None
        
    return rearranged_str


def main():
  print("Rearranged string:  " + rearrange_string("aappp"))
  print("Rearranged string:  " + rearrange_string("Programming"))
  print("Rearranged string:  " + rearrange_string("aapa"))


main()

