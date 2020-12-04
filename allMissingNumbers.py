# ========================
# Find All Missing Numbers
# ========================

# We are given an unsorted array containing numbers taken from 
# the range 1 to ‘n’. The array can have duplicates, which means 
# some numbers will be missing. Find all those missing numbers.


def find_missing_numbers(nums):
    missingNumbers = []
    i = 0
    while i < len(nums):
        correctIndex = nums[i] - 1
        # if the element at i doesn't belong there and the element
        # at its correct index isn't a duplicate
        if nums[i] != nums[correctIndex]:
            nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            missingNumbers.append(i+1)

    return missingNumbers

def main():
  print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
  print(find_missing_numbers([2, 4, 1, 2]))
  print(find_missing_numbers([2, 3, 2, 1]))

main()