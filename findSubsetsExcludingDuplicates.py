def find_subsets(nums):
    previous_num, subsets = None, []
    nums.sort() # O(nlogn)
    
    subsets.append([])
    n = len(nums)
    # for each number in input set
    for i in range(n):
        current_num = nums[i]
        # if it's not a duplicate number, create all permutation sets with it
        if current_num != previous_num:
            # create a copy of current subsets, add current_num to all sets in that copy
            # add modified copy to original list of subsets
            for j in range(len(subsets)):
                this_set = list(subsets[j])
                this_set.append(current_num)
                subsets.append(this_set)
        previous_num = current_num
    return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
