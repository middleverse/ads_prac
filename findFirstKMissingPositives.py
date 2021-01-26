def find_first_k_missing_positive(nums, k):
    missingNumbers = []
    i, n = 0, len(nums)
    largest = -1
    while i < n:
        j = nums[i] - 1 # where elem at i should be
        largest = max(largest, nums[i])
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if k == 0:
            break
        if nums[i] != i + 1:
            missingNumbers.append(i + 1)
            k -= 1
    
    while k > 0:
        missingNumbers.append(largest + 1)
        largest += 1
        k -= 1

    return missingNumbers


def main():
  print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
  print(find_first_k_missing_positive([2, 3, 4], 3))
  print(find_first_k_missing_positive([-2, -3, 4], 2))


main()