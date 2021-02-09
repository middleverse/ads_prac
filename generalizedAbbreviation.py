from collections import deque

class AbbreviatedWord:
  def __init__(self, str, start,  count):
    self.str = str
    self.start = start
    self.count = count

def generate_generalized_abbreviation(word):
    word_len = len(word)
    result = []
    queue = deque()
    queue.append(AbbreviatedWord(list(), 0, 0))
    while queue:
        ab_word = queue.popleft()
        # if we've reached an abreviated permutation of len word_len
        if ab_word.start == word_len:
            if ab_word.count != 0:
                ab_word.str.append(str(ab_word.count))
            result.append(''.join(ab_word.str))
        else:
            # skip a char and add to count
            queue.append(AbbreviatedWord(list(ab_word.str), ab_word.start + 1, ab_word.count + 1))
            # abbreviate a char, set count to 0
            if ab_word.count != 0:
                ab_word.str.append(str(ab_word.count))
            ab_word.str.append(word[ab_word.start])
            queue.append(AbbreviatedWord(list(ab_word.str), ab_word.start + 1, 0))
    print(len(result))
    return result

def main():
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("BAT")))
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("code")))

main()