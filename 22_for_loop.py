def print_numbers_in_range():
  for number in range(0, 10):
    print(f"This number is {number}")


print_numbers_in_range()


###while version

def print_numbers_in_range_with_a_while():
  number = 0
  while number < 10:
    print(f"This number is {number}")
    number = number + 1


print_numbers_in_range_with_a_while()

# * Summarising: Using a loop to distil a list into one
#   value.

# * Mapping: Using a loop to convert each item to another
#   item.

# * Filtering: Using a loop to pick out only some items from
#   a list.
