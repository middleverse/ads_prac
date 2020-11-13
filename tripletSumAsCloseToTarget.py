import math

def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smallest_delta = math.inf

    # iterate through array elements
    for index in range(len(arr)):
        left, right = index + 1, len(arr) - 1
        
        # find sum closest to target sum
        while left < right:
            # calculate current sum
            current_sum = arr[index] + arr[left] + arr[right]
            smallest_delta = min(smallest_delta, abs(current_sum - target_sum))
            print(smallest_delta)
            # shift left and right pointers appropriately
            if current_sum < target_sum:
                left += 1
            elif current_sum > target_sum:
                right -= 1
            else: # the smallest diff we can find, return target_sum
                return target_sum 
    
    # return the sum of the TRIPLET
    return target_sum - smallest_delta

def main():
  print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print()
  print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print()
  print(triplet_sum_close_to_target([1, 0, 1, 1], 100))

main()