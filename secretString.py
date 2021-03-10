from heapq import *

def secretString(triplets):
    '''
    Returns the secret string synthesized through working with triplets list
    '''
    max_heap, freq_map = [], dict()

    # build map, key = char, value = set of all chars that come after it
    for triplet in triplets:
        char1, char2, char3 = triplet[0], triplet[1], triplet[2]
        freq_map[char1] = freq_map.get(char1, set())
        freq_map[char1].add(char2)
        freq_map[char1].add(char3)
        freq_map[char2] = freq_map.get(char2, set())
        freq_map[char2].add(char3)
    
    # recursively calculate the weight of each character
    # the character with the lowest weight will be last 
    # the character with the greatest weight will be first
    # and all chars in between will be sorted as such
    visited = dict()
    for key, value in freq_map.items():
        traverseGraph(freq_map, key, visited)
    result = list(visited.keys())
    result.reverse()
    return ''.join(result)

def traverseGraph(freq_map, current_char, visited):
    '''
    Helper function to recursively figure out weight of given char
    '''
    chars = freq_map.get(current_char, None)
    # if there are no children, return 0, mark as visited
    if not chars:
        visited[current_char] = 0
        return 0

    # if current char's weight has been calculated, return it
    if visited.get(current_char, None) is not None:
        return visited[current_char]
    
    # calculate weights for all chars that come after current "char"
    weight = 0
    for c in chars:
            weight += traverseGraph(freq_map, c, visited)
    weight += len(chars)
    visited[current_char] = weight
    return weight 

def main():
    secret_1 = "whatisup"
    triplets_1 = [
        ['t','u','p'],
        ['w','h','i'],
        ['t','s','u'],
        ['a','t','s'],
        ['h','a','p'],
        ['t','i','s'],
        ['w','h','s']
    ]
    s = secretString(triplets_1)
    print('Triplet found:', s)
    print('-> Which is %s' % 'Correct' if secret_1 == s else 'Incorrect')
    
main()