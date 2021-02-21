def search_next_letter(letters, key):
    # Assume array is circular
    start, end = 0, len(letters) - 1
    if ord(letters[start]) > ord(key) or ord(key) > ord(letters[end]):
        return letters[start]

    while start <= end:
        mid = start + ((end - start) // 2)
        # since we want a higher order than the order of the key
        # move up if key == mid letter
        if ord(key) >= ord(letters[mid]):
            start = mid + 1
        # if key < mid letter
        else:
            end = mid - 1

    return letters[start % len(letters)]


def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()
