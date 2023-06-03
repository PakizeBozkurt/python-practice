def add_cats_repeatedly(word_list, count):
    i = 0
    while i < count:
        word_list.append('cats')
        i = i + 1
    return word_list


# check_that_these_are_equal(
#     add_cats_repeatedly([], 3), ['cats', 'cats', 'cats'])
# check_that_these_are_equal(
#     add_cats_repeatedly(['dogs'], 2), ['dogs', 'cats', 'cats'])

print("")
print("Function: add_cats_repeatedly")
