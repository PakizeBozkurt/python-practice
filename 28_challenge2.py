# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."


def report_long_words(words):
  long_words = extract_long_words(words)
  no_hyphens = reject_hyphens_words(long_words)
  short_if_longer = short_very_long_words(no_hyphens)
  return format_long_word_report(short_if_longer)

  print("")


print("Function: report_long_words")
