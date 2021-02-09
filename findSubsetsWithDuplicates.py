def find_subsets(nums):
    subsets = []
    nums.sort()
    subsets.append([])
    start_index, end_index = 0, 0
    # go through each number
    for i in range(len(nums)):
        # we'll want start_index to be 0 everytime, except for when 
        # we're dealing with a duplicate element
        # in that case we'll want to start at the index of the first element 
        # in the subset created in the last iteration (end_index of last iter + 1)
        start_index = 0
        if i > 0 and nums[i] == nums[i-1]:
            start_index = end_index + 1
        end_index = len(subsets) - 1
        # add current_num to each subset included in selected range
        for j in range(start_index, end_index + 1):
            this_set = list(subsets[j])
            this_set.append(nums[i])
            subsets.append(this_set)
    return subsets

def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
