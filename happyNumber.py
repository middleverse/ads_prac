# =================
# Find Happy Number 
# =================

# PROBLEM STATEMENT
# Any number will be called a happy number if, after repeatedly 
# replacing it with a number equal to the sum of the square of 
# all of its digits, leads us to number ‘1’. All other (not-happy) 
# numbers will never reach ‘1’. Instead, they will be stuck in a 
# cycle of numbers which does not include ‘1'.

def find_square_sum(num):
    sum = 0
    while(num > 0):
        digit = num % 10 # get current digit
        sum += digit * digit
        num //= 10 # divide by 10, keep the int value only
    return sum

def find_happy_number(num):
    fast, slow = num, num
    # loop will only break when slow is equal to fast
    # either they will both be 1 when the loop breaks
    # or they will both be a number other than 1
    while True:
        slow = find_square_sum(slow)
        fast = find_square_sum(find_square_sum(fast))
        if slow == fast:
            break
    return slow == 1

def main():
    print(find_happy_number(23))
    print(find_happy_number(12))

main()
