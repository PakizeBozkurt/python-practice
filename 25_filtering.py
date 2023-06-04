raw_ages = [32, 40, None, 1, 32]

clean_ages = []  # This is our accumulator again

for age in raw_ages:  # We go through each age
  # We combine a for with an if to remove 'None' items
  if age != None:
    clean_ages.append(age)

print(raw_ages)
print(clean_ages)


####



def only_positive_numbers(numbers):
  clean_negs = []

  for number in clean_negs:
    if number > 0:
     clean_negs.append(number)

  return clean_negs


print("")
print("Function: only_positive_numbers")
# check_that_these_are_equal(
#     only_positive_numbers([-4, 4, -3, 3]), [4, 3])
# check_that_these_are_equal(
#     only_positive_numbers([-100]), [])
