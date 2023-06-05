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
  #Filter in the words that are 10 characters long
  long_words = extract_long_unhyphenated_words(words)
  #Filter out those that contain hyphens
#   without_hyphens = reject_hyphenated_words(long_words)
  #Map the ones thatover 15 characters to the shortened
  shortened_if_longer = shorten_very_long_words(long_words)
  #Summarise to a string report
  return format_long_word_report(shortened_if_longer)


def extract_long_unhyphenated_words(words):
  long_words = []
  for word in words:
    if len(word) > 10 and "-" not in word:
      long_words.append(word)
    return long_words


print(extract_long_unhyphenated_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
]))

# def reject_hyphenated_words(words):
#     long_words = []
#     for word in words:
#         if "-" not in word:
#             long_words.append(word)
#     return long_words


# print(reject_hyphenated_words([
#     'hello',
#     'nonbiological',
#     'Kay',
#     'this-is-a-long-word',
#     'antidisestablishmentarianism'
# ]))

def shorten_very_long_words(words):
    processed_words = []
    for word in words:
        if len(word) > 15:
            shortened_word = word[0:15] + "..."
            processed_words.append(shortened_word)
        else:
         processed_words.append(word)
    return processed_words    


print(shorten_very_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
]))

def format_long_word_report(long_words):
    report = "These words are quite long: "
    return report + ", ".join(long_words)

   
print("")
print("Function: report_long_words")
