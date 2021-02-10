def find_single_numbers(nums):
    n1xn2 = 0
    for num in nums:
        n1xn2 ^= num

    # find the right most set bit of n1xn2
    rightmost_set_bit = 1
    while (rightmost_set_bit & n1xn2) == 0:
        rightmost_set_bit = rightmost_set_bit << 1
    num1, num2 = 0, 0
    # divide all nums into two groups, with rms set and not set
    # for both groups, XOR all them elemnts and we're left with
    # and num2 as the two numbers in each group
    for num in nums:
        if rightmost_set_bit & num:
            num1 ^= num
        else:
            num2 ^= num
    return [num1, num2]


def main():
  print('Single numbers are:' +
        str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
  print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))

main()
