def calculate_bitwise_complement(n):
    number_of_bits = 0
    n_copy = n
    
    # count number of bits
    while n_copy > 0:
        number_of_bits += 1
        n_copy = n_copy >> 1
    
    # now that we have number of bits, shift one more, then subtract
    all_bits_set = pow(2, number_of_bits) - 1
    
    # XOR n with all bits set to get complement
    return n ^ all_bits_set

def main():
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))

main()