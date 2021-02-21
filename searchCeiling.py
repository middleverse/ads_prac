def search_ceiling_of_a_number(arr, key):
    start, end = 0, len(arr) - 1
    # assumption: array in sorted order, ascending
    if key > arr[end]:
        return -1

    while start <= end:
        mid = start + ((end - start) // 2)
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            return mid
    return start


def main():
  print(search_ceiling_of_a_number([4, 6, 10, 20, 340], 6))
  print(search_ceiling_of_a_number([1, 3, 8, 10, 15, 16], 12))
  print(search_ceiling_of_a_number([4, 6, 10], 17))
  print(search_ceiling_of_a_number([4, 6, 10], -1))


main()
