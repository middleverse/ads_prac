def find_missing_number(nums):
    # do it using XOR to avoid integer overflow in
    n = len(nums) + 1
    # XOR all numbers from 1 to n
    x1 = 1
    for i in range(2, n + 1):
        x1 = x1 ^ i
    # XOR all numbers in nums
    x2 = nums[0]
    for j in range(1, n - 1):
        x2 = x2 ^ nums[j]
    return x1 ^ x2

def main():
    arr = [1, 5, 2, 6, 4] 
    print('Missing number is:' + str(find_missing_number(arr)))

main()
