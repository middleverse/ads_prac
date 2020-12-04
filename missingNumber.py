# ===================
# Find Missing Number
# ===================

def find_missing_number(nums):
    i, n = 0, len(nums)
    while i < n:
        correctIndex = nums[i]
        # we won't worry about element n (it will be discarded)
        if nums[i] < n and nums[i] != i:
            nums[i], nums[correctIndex] = nums[correctIndex], nums[i] # swap
        else:
            i += 1

    # first number that doesn't equal its index is our missing number
    for i in range(n):
        if nums[i] != i:
            return i
    # otherwise the largest number is
    return n     
       
def main():
  print(find_missing_number([4, 0, 3, 1]))
  print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()