def find_subsets(nums):
    subsets = []
    
    subsets.append([])
    for num in nums:
        n = len(subsets)

        for i in range(n):
            this_set = list(subsets[i]) # makes a deep copy
            this_set.append(num)
            subsets.append(this_set)

    return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
