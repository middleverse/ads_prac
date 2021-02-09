from collections import deque

def find_permutations(nums):
    result = []
    set_length = len(nums)
    permutations = deque()
    permutations.append([])
    # iterate over each num
    for num in nums:
        n = len(permutations)
        # add num to each set in permutations so far
        for _ in range(n):
            old_permutation = permutations.popleft()
            # add current num to all positions in all old_permutation
            for j in range(len(old_permutation) + 1):
                new_permutation = list(old_permutation)
                new_permutation.insert(j, num)
                # if we're inserting the last number, we'll have our final sets
                if len(new_permutation) == set_length:
                    result.append(new_permutation)
                # else, we're at a previous stage
                else:
                    permutations.append(new_permutation)
    print(len(result))
    return result


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5, 7])))


main()
