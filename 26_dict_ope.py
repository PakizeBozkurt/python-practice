def count_words_by_length(words):
  word_len_freq = {}
  for word in words:
    word_len = len(word)
    if word_len not in word_len_freq:
      word_len_freq[word_len] = 1
    else:
      word_len_freq[word_len] = word_len_freq[word_len] + 1
  return word_len_freq


print("")
print("Function: count_words_by_length")

# check_that_these_are_equal(
#     count_words_by_length(["hat", "cat", "I", "bird"]),
#     {3: 2, 1: 1, 4: 1}
# )

# check_that_these_are_equal(
#     count_words_by_length(["four", "four", "four", "one"]),
#     {4: 3, 3: 1}
# )
