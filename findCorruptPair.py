def find_corrupt_numbers(nums):
    i = 0
    while i < len(nums):
        correctIndex = nums[i] - 1
        if nums[i] == nums[correctIndex]:
            i += 1
        else:
            nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
    
    for j in range(len(nums)):
        if nums[j] != j + 1:
            return [nums[j], j + 1]
    return [-1, -1]


def main():
  print(find_corrupt_numbers([3, 1, 2, 5, 2]))
  print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))


main()
