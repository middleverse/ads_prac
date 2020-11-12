# =========================
# Square Sorted Array Items
# =========================

# PROBLEM STATEMENT
# Given a sorted array, create a new array containing squares of 
# all the number of the input array in the sorted order.

# EXAMPLE
# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]
# Input: [-3, -1, 0, 1, 2]
# Output: [0 1 1 4 9] 

def make_squares(arr):
    squares = []
    left, right = 0, len(arr) - 1

    while left <= right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] *arr[right]
        if left_square >= right_square:
            squares.insert(0, left_square)
            left += 1
        else:
            squares.insert(0, right_square)
            right -= 1
        
    return squares
    
def main():
  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))

main()