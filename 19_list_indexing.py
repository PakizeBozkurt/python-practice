
def get_first_item(the_list):
  # Return the first item of the list
 return the_list[0]


# check_that_these_are_equal(
#     get_first_item(["a", "b", "c", "d", "e"]),
#     "a"
# )

# check_that_these_are_equal(
#     get_first_item([34, 44, 54, 64]),
#     34
# )

print("")
print("Function: get_first_item")

#####


def get_last_item(the_list):
  # Return the last item of the list
 return the_list[-1]


# check_that_these_are_equal(
#     get_last_item(["a", "b", "c", "d", "e"]),
#     "e"
# )

# check_that_these_are_equal(
#     get_last_item([34, 44, 54, 64]),
#     64
# )

print("")
print("Function: get_last_item")


#####



def get_items_between_one_and_three(the_list):
  # Return the section of the list between indexes one
  # and three
  return the_list[1:3]


# check_that_these_are_equal(
#     get_items_between_one_and_three(["a", "b", "c", "d", "e"]),
#     ["b", "c"]
# )

# check_that_these_are_equal(
#     get_items_between_one_and_three([34, 44, 54, 64]),
#     [44, 54]
# )

print("")
print("Function: get_items_between_one_and_three")
