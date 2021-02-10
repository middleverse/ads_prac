def flip_and_invert_image(matrix):
    row_len = len(matrix) # assuming square matrix  
    for row in matrix:
      for j in range((row_len + 1)//2):
        flipped_j = row_len - j - 1 
        row[j], row[flipped_j] = row[flipped_j] ^ 1, row[j] ^ 1

    return matrix

def main():
  print(flip_and_invert_image([[1,0,1], [1,1,1], [0,1,1]]))
  print(flip_and_invert_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

main()