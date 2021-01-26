def find_first_smallest_missing_positive(nums):
    i, n = 0, len(nums)
    while i < n:

        # CASES:
        # cur el is where it belongs, move on
        # cur el is negative, move on
        # cur el is greater than 1 + size of array, movee on
        # cur el is not where it belongs, shift cur el to where it does belong

        j = nums[i] - 1 # where i needs to go
        if nums[i] != i + 1 and nums[i] > 0 and nums[i] <= n:
            nums[i], nums[j] = nums[j], nums[i] # swap
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1: # found smallest missing
            return i + 1 
          
    return len(nums) + 1 # otherwise return largest
