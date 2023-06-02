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
