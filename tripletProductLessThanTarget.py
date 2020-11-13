
# PROBLEM STATEMENT
# Given an array with positive numbers and a target number, find all of 
# its contiguous subarrays whose product is less than the target number.


def find_subarrays(arr, target):
    result = []

    # iterate over all elements in arr
    for left in range(len(arr)):
        # current left element is less than target, add to list
        if arr[left] < target:
            result.append(arr[left])
        # current left element is larger than target, no more subarray left
        else:
            return result

        # start with product equals left element
        product = arr[left]
        temp_list = list()
        temp_list.append(arr[left])        
        right = left + 1    

        # iterate through array len starting from right
        while right < len(arr):
            product *= arr[right]
            # product is still smaller than target
            # update temp list, and add temp list to results
            if product < target:
                temp_list.append(arr[right])
                result.append(list(temp_list))
            # product is larger than target
            else:
                break
            right += 1

    return result

def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print()
  print(find_subarrays([8, 2, 6, 5], 50))

main()