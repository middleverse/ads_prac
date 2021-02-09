
from os import close


def generate_valid_parentheses(num):
    result = []
    # default_string = [0 for x in range(2*num)] # 1 open and 1 close bracket for each num
    generate_valid_parentheses_recursive(num, 0, 0, '', 0, result)
    return result


def generate_valid_parentheses_recursive(num, openCount, closeCount, current_str, index, result):
    if openCount == num and closeCount == num:
        result.append(current_str)
    else:
        # one option is to add open bracket, as long openCount < num
        if openCount < num:
            open_str = current_str
            open_str += '('
            generate_valid_parentheses_recursive(num, openCount + 1, closeCount, open_str, index + 1, result)
        # if not empty string and closeCount <
        if openCount > closeCount:
            close_str = current_str
            close_str += ')'
            generate_valid_parentheses_recursive(num, openCount, closeCount + 1, close_str, index + 1, result)

def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))


main()
