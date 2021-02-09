def find_letter_case_string_permutations(str):
    permutations = []
    find_letter_case_string_permutations_recursive(str, 0, [], permutations)
    return permutations

def find_letter_case_string_permutations_recursive(str, current_char_index, current_permutation, permutations):
    if current_char_index == len(str):
        curr_str_perm = "".join(current_permutation)
        permutations.append(curr_str_perm)

    else:
        current_char = str[current_char_index]
        new_permutation = list(current_permutation)
        if current_char.isdigit():
            new_permutation.append(current_char)
            find_letter_case_string_permutations_recursive(str, current_char_index + 1, new_permutation, permutations)
        else:
            uppercase_new_permutation = list(current_permutation)
            new_permutation.append(current_char)
            uppercase_new_permutation.append(current_char.upper())
            find_letter_case_string_permutations_recursive(str, current_char_index + 1, new_permutation, permutations)
            find_letter_case_string_permutations_recursive(str, current_char_index + 1, uppercase_new_permutation, permutations)    

def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()
