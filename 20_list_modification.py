print("")
print("Function: remove_item_from_list")


def remove_item_from_list(the_list, item):
    the_list.remove(item)
    return the_list


# check_that_these_are_equal(
#     remove_item_from_list(['a', 'b'], 'b'), ['a'])
# check_that_these_are_equal(
#     remove_item_from_list([3, 1], 3), [1])

######

print("")
print("Function: count_items_in_list")


def count_items_in_list(the_list, item):
  return the_list.count(item)


# check_that_these_are_equal(
#     count_items_in_list(['a', 'b', 'a'], 'a'), 2)
# check_that_these_are_equal(
#     count_items_in_list([4, 1, 4, 4], 4), 3)


###

print("")
print("Function: get_index_of_item")


def get_index_of_item(the_list, item):
  return the_list.index(item)


# check_that_these_are_equal(
#     get_index_of_item(['a', 'b', 'c'], 'b'), 1)
# check_that_these_are_equal(
#     get_index_of_item([33, 44, 55], 55), 2)


####

print("")
print("Function: reverse_list")


def reverse_list(the_list):
  the_list.reverse()
  return the_list


# check_that_these_are_equal(
#     reverse_list(['a', 'b', 'c']), ['c', 'b', 'a'])
# check_that_these_are_equal(
#     reverse_list([33, 44, 55]), [55, 44, 33])
