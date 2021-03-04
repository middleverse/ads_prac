def find_range(arr, key):
    result = [- 1, -1]
    start, end = 0, len(arr) - 1
    found = False

    while start <= end:
        mid = start + ((end - start) // 2)

        if key == arr[mid]:
            found = True
            break

        if key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    # find left and right boundaries   
    left = mid
    right = mid
    while left > 0 and arr[left] == arr[left - 1]:
        left -= 1
    while right < len(arr) - 1 and arr[right] == arr[right + 1]:
        right += 1

    return [left, right] if found else [-1 , -1]

def main():
  print(find_range([4, 6, 6, 6, 9], 6))
  print(find_range([1, 3, 8, 10, 15], 10))
  print(find_range([1, 3, 8, 10, 15], 12))


main()
