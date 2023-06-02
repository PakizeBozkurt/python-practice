print("")
print("Function: remove_item_from_list")


def remove_item_from_list(the_list, item):
    the_list.remove(item)
    return the_list


# check_that_these_are_equal(
#     remove_item_from_list(['a', 'b'], 'b'), ['a'])
# check_that_these_are_equal(
#     remove_item_from_list([3, 1], 3), [1])
