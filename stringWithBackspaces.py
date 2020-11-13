# =======================================
# Comparing Strings containing Backspaces
# =======================================

# PROBLEM STATEMENT
# Given two strings containing backspaces (identified by the character ‘#’), 
# check if the two strings are equal.

# EXAMPLE
# Input: str1="xy#z", str2="xzz#"
# Output: true
# Explanation: After applying backspaces the strings become "xz" and "xz" respectively.

def backspace_compare(str1, str2):
    i, j = len(str1) - 1, len(str2) - 1
    backspace_quota_1 = 0
    backspace_quota_2 = 0

    while (i > -1 and j > -1):
        # parse backspace if any        
        while str1[i] == '#':
            backspace_quota_1 += 1
            i -= 1
        while str2[j] == '#':
            backspace_quota_2 += 1
            j -= 1
        # get next char of str1 & str2
        while (backspace_quota_1 > 0):
            i -= 1
            backspace_quota_1 -= 1
        while (backspace_quota_2 > 0):
            j -= 1
            backspace_quota_2 -= 1
        # compare the two, if not equal, return False
        if str1[i] != str2[j]:
            return False
        i -= 1
        j -= 1
    # in the case that one string ends with the other string as a substring
    # we will go through the above while loop without returning False
    # a check for that:
    if i != j:
        return False
    # if we made it here, strings matched
    return True

def main():
  print(backspace_compare("xy#z", "xzz#"))
  print(backspace_compare("xy#z", "xyz#"))
  print(backspace_compare("xp#", "xyz##"))
  print(backspace_compare("xywrrmp", "xywrrmu#p"))

main()